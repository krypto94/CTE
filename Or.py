import numpy as np 

W = np.random.rand(2,2)*0.01
b = np.zeros((1,2))


X1 =np.zeros((1,2))
X2 =np.zeros((1,2))
X3 =np.zeros((1,2))
X4 =np.zeros((1,2))
X2[0,1] = 1
X3[0,0] = 1
X4[0,0] =1
X4[0,1] =1


X=[X1,X2,X3,X4]
Y = [0,1,1,1]
flag = 0
step_size = 1e-2
reg = 1e-2
for i in xrange(50):
	Score = np.dot(X[flag],W)+b
	
	exp_scores = np.exp(Score)
	probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
	print probs
	dscores = probs
	dscores[0,Y[flag]] = -1
	dW = np.dot(X[flag].T, dscores)
  	db = np.sum(dscores, axis=0, keepdims=True)
  
  	dW += reg*W
  	W += -step_size * dW
  	b += -step_size * db
  	flag = flag + 1
	if flag == 4:
		flag = 0 
Score = np.dot(X[0],W)+b
exp_scores = np.exp(Score)
probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
print probs