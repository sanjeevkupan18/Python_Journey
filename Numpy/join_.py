import numpy as np 
#Joining using concatenation
var=np.array([1,2,3,4])
var1=np.array([9,8,7,6])
join=np.concatenate((var,var1))
print(join)
print()

#2Dimension
var2=np.array([[1,2],[3,4]])
var3=np.array([[5,6],[7,8]])
new=np.concatenate((var2,var3),axis=1)  #joining along row axis =1
print(new)
print()

#stack function for joining with axis
var4=np.array([[1,2],[3,4]])
var5=np.array([[5,6],[7,8]])
new1=np.stack((var4,var5),axis=1)
new2=np.hstack((var4,var5)) #horizontal row concatenation
new3=np.vstack((var4,var5)) #vertical column concatenation
new4=np.dstack((var4,var5)) #height distance concatenation
print(new1)
print()
print(new2)
print()
print(new3)
print()
print(new4)