import numpy as np 

#For 1 Dimension
var1=np.array([9,8,7,6,5,4,3,2,1])
print(var1[0:9:2]) # start : stop : step
print(var1[ :7]) # start 0 end 7
print()

#For 2Dimension
var2=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(var2[1,1:]) #first 1 for row indexing and second 1 for element 7
print(var2[2,1:])