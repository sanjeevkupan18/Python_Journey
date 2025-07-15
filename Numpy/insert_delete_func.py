import numpy as np 
#insert function
var=np.array([1,2,3,4])
v=np.insert(var,2,40) # 2 index value 40
x=np.insert(var,(3,4),80)
print(v)
print(x)
print()

var1=np.array([[1,2,3],[4,5,6]])
v1=np.insert(var1,2,66,axis=1) #row
v2=np.insert(var1,2,[23,45],axis=1) #row two values at index 2
print(v1)
print(v2)
print()

var2=np.array([[9,8,7],[6,5,4]])
v3=np.append(var2,[[1,2,3]],axis=0)
print(v3)
print()

#delete
var3=np.array([1,2,3,4])
d=np.delete(var3,2)
print(d)