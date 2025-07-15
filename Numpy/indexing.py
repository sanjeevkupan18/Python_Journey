import numpy as np 
#For 1 Dimension
var1=np.array([1,2,3,4])
print(var1[1])
print(var1[-3])
print()

#For 2 Dimension
var2=np.array([[1,2,3],[4,5,6]]) #2Dimension
print(var2[0,1]) # 0 for first row and 1 for element indexing
print()

#For 3 Dimension
var3=np.array([[[1,2],[6,7],[4,5]]])
print(var3[0,2,1])  #0 for first block 2 for 3rd row and 1 for element 5 indexing
