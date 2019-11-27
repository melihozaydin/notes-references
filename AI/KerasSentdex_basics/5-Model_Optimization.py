import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import matplotlib.pyplot as plt
import time




gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))


x = pickle.load(open('x.pickle', 'rb'))
y = pickle.load(open('y.pickle', 'rb'))
x = x/255 # normalize


####
#customizible parameters
'''
dense_layers = [0,1,2]
layer_sizes = [32,64,128]
conv_layers = [1, 2, 3]
'''

####
dense_layers = [0]
layer_sizes = [64]
conv_layers = [3]

for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME = '{}-conv-{}-nodes-{}-dense-{}'.format(conv_layer, layer_size, dense_layer, int(time.time()))
            tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))  #Define Callback with logdir
            print(NAME)
            model = Sequential()
            model.add(Conv2D(layer_size, (3, 3), input_shape = x.shape[1:]))
            model.add(Activation('relu'))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            for l in range(conv_layer):
                model.add(Conv2D(layer_size, (3, 3)))
                model.add(Activation('relu'))
                model.add(MaxPooling2D(pool_size=(2 ,2)))
            
            model.add(Flatten())
            for l in range(dense_layer):
                model.add(Dense(layer_size))
                model.add(Activation('relu'))

            model.add(Dense(1))
            model.add(Activation('sigmoid'))


            model.compile(optimizer='adam', 
                        loss='binary_crossentropy', 
                        metrics=['accuracy'])

            ## Run " tensorboard --logdir=./ " 
            ## from logs dir from terminal

            model.fit(x, y, batch_size=32, epochs=10, validation_split=0.1, 
                    callbacks=[tensorboard])
model.save('{}.model'.format(NAME))
