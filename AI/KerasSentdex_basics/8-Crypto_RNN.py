import pandas as pd
from sklearn import preprocessing
from collections import deque
import numpy as np
import random
import time

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import CuDNNLSTM, BatchNormalization
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.callbacks import ModelCheckpoint

# how long of a preceeding sequence to collect for RNN
SEQ_LEN = 60
# how far into the future are we trying to predict?
FUTURE_PERIOD_PREDICT = 3
RATIO_TO_PREDICT = 'BTC-USD'
EPOCHS = 10
BATCH_SIZE = 64
NAME = f"{RATIO_TO_PREDICT}-{SEQ_LEN}-SEQ-{FUTURE_PERIOD_PREDICT}-PRED-{int(time.time())}"


def classify(current, future):
    # if the future price is higher than the current, that's a buy, or a 1
    if float(future) > float(current):
        return 1
    else:  # otherwise... it's a 0!
        return 0


####
# Dataset Formatting
####

'''
df = pd.read_csv('crypto_data/LTC-USD.csv', names=['time', 'low', 'high',
                                                   'open', 'close', 'volume'])
print(df.head())
'''

main_df = pd.DataFrame()

ratios = ['BTC-USD', 'LTC-USD', 'ETH-USD', 'BCH-USD']

for ratio in ratios:
    # print(ratio)
    # split away the ticker from the file-name

    # get the full path to the file.
    dataset = f"crypto_data/{ratio}.csv"
    # read in specific file
    df = pd.read_csv(dataset, names=['time', 'low', 'high', 'open',
                                     'close', 'volume'])
    # rename volume and close to include the ticker
    # so we can still which close/volume is which:
    df.rename(columns={'close': f'{ratio}_close', 'volume': f'{ratio}_volume'},
              inplace=1)

    # set time as index so we can join them on this shared time
    df.set_index('time', inplace=True)
    # ignore the other columns besides price and volume
    df = df[[f'{ratio}_close', f'{ratio}_volume']]

    # print(df.head())

    if len(main_df) == 0:  # if the dataframe is empty
        main_df = df  # then it's just the current df
    else:
        main_df = main_df.join(df)  # otherwise, join this data to the main one

# if there are gaps in data, use previously known values
main_df.fillna(method="ffill", inplace=True)
main_df.dropna(inplace=True)
# print(main_df.head())  # how did we do??

main_df['future'] = main_df[f'{RATIO_TO_PREDICT}_close'].shift(-FUTURE_PERIOD_PREDICT)
main_df['target'] = list(map(classify,
                             main_df[f'{RATIO_TO_PREDICT}_close'],
                             main_df['future']))

# print(main_df[[f'{RATIO_TO_PREDICT}_close', 'future', 'target']].head(10))

# part-1 end
# seperating out of samples (test data)
# you need to seperate from the end of the sequence

###
# PART-2
###


def preprocess_df(df):
    # scaling
    df = df.drop('future', 1)
    for col in df.columns:
        if col != 'target':
            # pct change "normalizes" the different currencies
            # (each crypto coin has vastly diff values,
            # we're really more interested in the other coin's movements)
            df[col] = df[col].pct_change()
            df.dropna(inplace=True)  # drop NAN's
            # scale to 0-1 interval
            df[col] = preprocessing.scale(df[col].values)
    df.dropna(inplace=True)

    sequential_data = []  # this is a list that will CONTAIN the sequences

    # These will be our actual sequences. They are made with deque,
    # which keeps the maximum length by
    # popping out older values as new ones come in
    prev_days = deque(maxlen=SEQ_LEN)

    # df.values converts df to list of lists
    # but it still contains value
    for i in df.values:
        prev_days.append([n for n in i[:-1]])
        if len(prev_days) == 60:
            # put xtrain and ytrain
            sequential_data.append([np.array(prev_days), i[-1]])
    random.shuffle(sequential_data)

    buys = []
    sells = []
    for seq, target in sequential_data:
        if target == 0:
            sells.append([seq, target])
        elif target == 1:
            buys.append([seq, target])

    random.shuffle(buys)
    random.shuffle(sells)

    lower = min(len(buys), len(sells))

    buys = buys[:lower]
    sells = sells[:lower]

    sequential_data = buys+sells
    random.shuffle(sequential_data)

    X = []
    y = []

    for seq, target in sequential_data:
        X.append(seq)
        y.append(target)

    return np.array(X), y


times = sorted(main_df.index.values)  # get the times
# get the last 5% of the times
last_5pct = sorted(main_df.index.values)[-int(0.05*len(times))]

# make the validation data where the index is in the last 5%
validation_main_df = main_df[(main_df.index >= last_5pct)]
# now the main_df is all the data up to the last 5%
main_df = main_df[(main_df.index < last_5pct)]

print(main_df.head())

train_x, train_y = preprocess_df(main_df)
validation_x, validation_y = preprocess_df(validation_main_df)

print(f"train_data: {len(train_x)} validation: {len(validation_x)}")
print(f"Dont buys: {train_y.count(0)} buys: {train_y.count(1)}")
print(f"Val_dont_buys: {validation_y.count(0)} val_Buys: {validation_y.count(1)}")

model = Sequential()
model.add(CuDNNLSTM(128, input_shape=(train_x.shape[1:]),
                    return_sequences=True))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(CuDNNLSTM(128, input_shape=(train_x.shape[1:]),
                    return_sequences=True))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(CuDNNLSTM(128, input_shape=(train_x.shape[1:])))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(2, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6)

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

tensorboard = TensorBoard(log_dir=f'logs/{NAME}')

filepath = 'RNN_Final-{epoch:02d}-{val_acc:.3f}'
checkpoint = ModelCheckpoint("models/{}.model".format(filepath,
                             monitor='val_acc', verbose=1,
                             save_best_only=True, mode='max'))  # save best

# Train model
history = model.fit(
    train_x, train_y,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    validation_data=(validation_x, validation_y),
    callbacks=[tensorboard, checkpoint],
)

# Score model
score = model.evaluate(validation_x, validation_y, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
# Save model
model.save("models/{}".format(NAME))