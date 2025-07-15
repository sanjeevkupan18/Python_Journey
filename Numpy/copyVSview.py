import numpy as np 
#copy function
var=np.array([1,2,3,4,5]) #copy a new array original array data remain safe
co=var.copy()
print(var)
print(co)
print()

#View function
var1=np.array([9,8,7,6,5])
vi=var1.view() #omit the original data to create new array
print(var1)
print(vi)