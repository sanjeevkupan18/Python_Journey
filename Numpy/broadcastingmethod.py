import numpy as np 
#broadcasting = performing any operation between two array must satisfy the condition of ixj(j=1 in both array)

var1=np.array([1,2,3]) #1x3 array
print(var1)
print(var1.shape)
print()

var2=np.array([[1],[2],[3]]) #2dimension array having 3row and 1 column 3x1 array
print(var2)
print(var2.shape)
print()

var3=var1+var2
print(var3)
print(var3.shape)