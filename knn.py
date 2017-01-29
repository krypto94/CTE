import numpy as np 
f=file("/home/rishabh/Desktop/CTE/KNN_data.bin","rb")
data=np.load(f)

test = np.array((0.36,0.255))
length = np.empty((1000,2))

for i in xrange(1000):
	length[i,0] = np.linalg.norm(test - data[i,0:2])
	length[i,1] = data[i,2]

sorted_length = length[np.argsort(length[:, 0])]
K = 5
unique ,counts = np.unique(sorted_length[:K,1],return_counts= True)
dict = dict(zip(unique, counts))
print dict
a = max(dict.iterkeys(), key=(lambda k: dict[k]))
print a