# I have applied sigmoid function
# I have taken bias in xi (i=1,2,3,4)
# like - x1 = [0, 0, 1]
# Y = array of desired output
# n = learning rate
# W = weights
# y_in = sigma function
# tmp = 1/(1+e^(-x))
# e matrix to store error.
# d = error * derivative of sigmoid function


import numpy as np
import math

W = np.random.rand(3,1)*0.01

e = np.zeros((1000000,4))
y = np.zeros((1000000,4))
X1 =np.zeros((1,3))
X2 =np.zeros((1,3))
X3 =np.zeros((1,3))
X4 =np.zeros((1,3))

X1[0,2] = 1

X2[0,1] = 1
X2[0,2] = 1

X3[0,0] = 1
X3[0,2] = 1

X4[0,0] = 1
X4[0,1] = 1
X4[0,2] = 1

X=[X1,X2,X3,X4]
Y = [0,0,0,1]

n = 0.9
for i in xrange(1000000):
	for j in xrange(4):
		y_in = np.dot(X[j],W)
		tmp = 1 / (1 + math.exp(-1*y_in))
		y[i,j] = tmp
		e[i,j] = Y[j] - y[i,j]
		d = e[i,j]*tmp*(1-tmp)
		W = W + n*d*(np.reshape(X[j], (3,1))) #updating weights.
print e
print y
print W
