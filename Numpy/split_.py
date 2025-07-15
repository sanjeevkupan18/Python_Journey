import numpy as np 

var=np.array([1,2,3,4,5,6])
ar=np.array_split(var,3)
print(ar) #data type list
print(ar[0]) # 1 array elements
print()

# 2 Dimension
var2=np.array([[1,2],[3,4],[5,6]])
ar1=np.array_split(var2,3)
ar2=np.array_split(var2,3,axis=1)
print(ar1)
print()
print(ar2)