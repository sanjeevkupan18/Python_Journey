import numpy as np 
# shuffle function
var=np.array([1,2,3,4,5,6]) #shuffle the data
np.random.shuffle(var)
print(var)
print()

# unique function
var1=np.array([1,2,3,3,4,1])
x=np.unique(var1,return_index=True,return_counts=True) #returns index of unique elements
print(x)                                              # counts the repititon of elements
print()

# resize function
var2=np.array([1,2,3,4,5,6])
y=np.resize(var2,(2,3))   # 2 row and 3 column 
print(y)
print()

# flatten function
var3=np.array([1,2,3,4,5,6])
y=np.resize(var3,(2,3)) 

print(y.flatten()) #change the 2 dimension array to 1 dimension
print(y.flatten(order="F")) # different order C,F,A,K
print(np.ravel(y,order="K"))

