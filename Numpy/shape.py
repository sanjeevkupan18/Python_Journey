import numpy as np 
#Shape Function

var=np.array([[1,2,3,4],[2,3,4,5]])  #2Row and 4Column
print(np.shape(var))
print()

var1=np.array([1,2,3,4],ndmin=4) #1Row 3 times and 4Column
print(var1)
print(np.shape(var1))
print()

#Reshape Function
var2=np.array([1,2,3,4,5,6,7,8,9])
print(var2)
print(var2.ndim)
print()

x=var2.reshape(3,3)
print(x)
print(x.ndim)
print()

#3Dimension
var3=np.array([1,2,3,4,5,6,7,8,9,10,11,21])
print(var3.ndim)
print()
y=var3.reshape(2,3,2)
print(y)
print(y.ndim)
print()

#3dimension to 1Dimension conversion
one=y.reshape(-1)
print(one)
print(one.ndim)