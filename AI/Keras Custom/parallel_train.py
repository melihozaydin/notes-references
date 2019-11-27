from tensorflow.keras.layers import *
from tensorflow.keras.models import Model, Sequential
import numpy as np
import random
import test
index=[]
for i in range(10):
    index.append(random.sample(range(0, 201), 10))
x_tr=[]
y_tr=[]
x_te=[]
y_te=[]

aa = test.train_data(index[0])
X_train0, Y_train0, X_Test0, Y_Test0 = test.ddata(aa)

aa = test.train_data(index[1])
X_train1, Y_train1, X_Test1, Y_Test1 = test.ddata(aa)

aa = test.train_data(index[2])
X_train2, Y_train2, X_Test2, Y_Test2 = test.ddata(aa)

aa = test.train_data(index[3])
X_train3, Y_train3, X_Test3, Y_Test3 = test.ddata(aa)

aa = test.train_data(index[4])
X_train4, Y_train4, X_Test4, Y_Test4 = test.ddata(aa)

aa = test.train_data(index[5])
X_train5, Y_train5, X_Test5, Y_Test5 = test.ddata(aa)

aa = test.train_data(index[6])
X_train6, Y_train6, X_Test6,Y_Test6 = test.ddata(aa)

aa = test.train_data(index[7])
X_train7, Y_train7, X_Test7, Y_Test7 = test.ddata(aa)

aa = test.train_data(index[8])
X_train8, Y_train8, X_Test8, Y_Test8 = test.ddata(aa)

aa = test.train_data(index[9])
X_train9, Y_train9, X_Test9, Y_Test9 = test.ddata(aa)


m=test.get_model()
inp0=Input((5,10,10,1))
inp1=Input((5,10,10,1))
inp2=Input((5,10,10,1))
inp3=Input((5,10,10,1))
inp4=Input((5,10,10,1))
inp5=Input((5,10,10,1))
inp6=Input((5,10,10,1))
inp7=Input((5,10,10,1))
inp8=Input((5,10,10,1))
inp9=Input((5,10,10,1))

out0=m(inp0)
out1=m(inp1)
out2=m(inp2)
out3=m(inp3)
out4=m(inp4)
out5=m(inp5)
out6=m(inp6)
out7=m(inp7)
out8=m(inp8)
out9=m(inp9)

model = Model([inp0,inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9],[out0,out1,out2,out3,out4,out5,out6,out7,out8,out9])
model.compile(optimizer='adam', loss='mse')
model.fit([X_train0,X_train1,X_train2,X_train3,X_train4,X_train5,X_train6,X_train7,X_train8,X_train9],[Y_train0,Y_train1,Y_train2,Y_train3,Y_train4,Y_train5,Y_train6,Y_train7,Y_train8,Y_train9], epochs = 50)

ypred0,ypred1,ypred2,ypred3,ypred4,ypred5,ypred6,ypred7,ypred8,ypred9 = model.predict([X_Test0,X_Test1,X_Test2,X_Test3,X_Test4,X_Test5,X_Test6,X_Test7,X_Test8,X_Test9])
print(ypred0.shape)