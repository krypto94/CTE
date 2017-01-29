import numpy as np 
data=np.random.rand(1000,3)
flag =1
for i in xrange(1000):
	data[i,2] = flag
	flag = flag + 1
	if(flag == 4):
		flag = 1
		
f=file("/home/rishabh/Desktop/CTE/KNN_data.bin","wb")
np.random.shuffle(data)
np.save(f,data)
f.close()
f=file("/home/rishabh/Desktop/CTE/KNN_data.bin","rb")
dat = np.load(f)
print dat.shape	