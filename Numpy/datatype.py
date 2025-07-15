import numpy as np 
x=np.array([1,2,3,4])
print(x.dtype)  #dtype function prints the data type of the variable
 
y=np.array([1,2,3],dtype=np.float16) #converting int64 to float16
print(y.dtype)

x1=np.float16(x) #another way to change data type using new variable
print(x1)
print(x1.dtype)


z=np.array([2,3,4])
z1=z.astype(float) #astype function converts data type directly
print(z1.dtype)