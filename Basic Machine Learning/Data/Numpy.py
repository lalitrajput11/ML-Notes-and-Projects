import numpy as np

# aa = np.array(32)
# print(aa.ndim)
# print(aa.shape)
# print(aa.size)

# a1 = np.array([[1,2,3],[2,3,4]])
# print(a1.ndim)
# print(a1.shape)
# print(a1.size)

# a2 = np.array([[[1,2,3],[2,3,4],[4,5,6]]],dtype=float)

# print(a2.shape)  #1,3,3
# print(a2.size)   #9
# print(a2.ndim)  #3
# print(a2.dtype)

# a3 = np.zeros((3,4))
# a3 =np.ones((2,3))
# d = np.arange(10,25,5)
# print(d)

# e = np.linspace(2,9,7)
# print(e)
# a =np.full((2,3,3),7)
# print(a)

# r = np.eye(2,2)
# print(r)
# print(a3)
# print(a3.ndim)

# s = np.empty((3,2))
# print(s)

# f = np.random.random((2,3))
# print(f)
# # print(len(f))
# print(f.astype(int))

# a= np.array((2,4),dtype=int)
# a.astype(dtype=float)

# print(a)
# print(a.dtype)

# x = np.array(["Hello","World !"],dtype="U5")
# print(x)
# print(x.dtype)

# x=np.random.random((2,3))
# print(x)
# print(x.astype(int))

# print(x+5)
# y = np.full((2,2),6)
# print(y)
# k = np.eye((2,2))
# k = k.astype(int)
# print(k)

# print(np.__version__)
# print(np.show_config())
# print(np.zeros(10))
# Z = np.zeros((10,10))
# print(Z)
# print("%d bytes" % (Z.size * Z.itemsize))

# z= np.zeros((10,10))
# print(z)
# print("%d bytes" % (z.size*z.itemsize))

# z= np.zeros(10)
# z[4] =1
# print(z)

# z = np.arange(10,50)
# print(z)

# print(np.arange(10,1,-1))

# z = np.arange(10)
# print(z)
# print(z[::-1])

# x = np.eye(4)
# print(x)
# print(x.dtype)

# print(f" size :  {(x.size * x.itemsize)} bytes") 

# x = np.arange(9).reshape(3,3)
# print(x)
# print(x.T)

# x = np.array([1,2,3,4,5,6]).reshape(2,3)
# print(x)
# print(x.T)

# nz = np.nonzero([1,2,0,0,4,0])
# print(nz)

# x = np.random.randint((3,4))
# print(x)
# Source - https://stackoverflow.com/q
# Posted by lmjohns3, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-23, License - CC BY-SA 3.0
# Source - https://stackoverflow.com/q
# Posted by lmjohns3, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-23, License - CC BY-SA 3.0

import numpy as np

# print randon interger number

# x = np.random.randint(0,10,size=(3,4))
# print(x)

# x = np.random.randint(0,100,size =10)
# print(x)
# print("Maximum value:",np.max(x))
# print("Minimum value:",np.min(x))
# print("Mean value:",np.mean(x))
# print("Median value:",np.median(x))
# print("Standard Deviation:",np.std(x))
# print("Variance:",np.var(x))
# print("25th Percentile:",np.percentile(x,25))
# print("50th Percentile:",np.percentile(x,50))
# print("75th Percentile:",np.percentile(x,75))  
# print("sorted array:",np.sort(x))


# x = np.random.randint(0,100,size =10)
# print(x)
# print(np.random.seed(0)) # seed what it does it

# print(np.random.randint(0,100,size=10))
# print(np.random.randint(0,100,size=(2,2)))

# Z = np.ones(5)
# print(Z)
# Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
# print(Z)
# z = np.ones((3,3))
# print(z)
# z= np.pad(z, pad_width=1,mode='constant', constant_values=4)
# print(z)

# indexing and slicing
# a = np.array([1,2,3,4,5,6,7,8,9])
# print(a[2:5]) #3,4,5
# print(a[::2])  #1,3,5,7,9
# print(a[-3:]) #7,8,9
# print(a[::-1])     #9,8,7,6,5,4,3,2,1
# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b[0:2,1:3])  #2,3 5,6
# print(b[1:,::2])   #4,6 7,9
# print(b[:,1])      #2 5 8   


# Z = np.ones((5,5))
# # Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
# # print(Z)
# print(Z)
# Z[:, [0, -1]] = 0
# Z[[0, -1], :] = 0
# print(Z)

# z = np.ones(5)
# print(z)
# z[0]=0
# z[-1]=0
# print(z)

# Z = np.random.randint((30),size=(6,6))
# print(Z) 

# print("\n")
# Z[1::2,::2]=1 #print odd row and odd column
# # Z[1::2,::2] = 1
# # Z[::2,1::2] = 1
# # print(Z)
# Z[0::2,1::2]=1  #print even row and even column


# print("\n")
# print(Z) 

# Z = np.diag(1+np.arange(4),k=-1)
# print(Z)

# print(np.diagflat([1,2,3,4],k=0))
# Z = np.zeros((8,8),dtype=int)
# Z[1::2,::2] = 1
# Z[::2,1::2] = 1
# print(Z)

print(np.unravel_index(99,(6,7,8)))
