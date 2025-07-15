import numpy as np 

var=np.matrix([[1,2],[4,5]])
var1=np.matrix([[1,2],[4,5]])
print(var)
print(type(var))
print()
print(var+var1)
print()
print(var*var1) #matrix multiplication
print(var.dot(var1)) #matrix dot mul
print()

# Functions in matrix
# Transpose function
var2=np.matrix([[1,2,3],[4,5,6]])
print(var2)
print(np.transpose(var2))
print(var2.T)  #shortcut for transpose
print()
#swapaxes function
print(np.swapaxes(var2,0,1))  #swapping axes 0 to 1
print()

# inverse 
var3=np.matrix([[1,2],[3,4]])
print(var3)
print(np.linalg.inv(var3))
print()

#power of matrix
var4=np.matrix([[1,2],[3,4]])
print(var4)
print(np.linalg.matrix_power(var4,2)) #power of matrix 2
print()
print(np.linalg.matrix_power(var4,0)) #if n=0 it gives inverse matrix
print()
print(np.linalg.matrix_power(var4,-2)) #if n is negative then inverse into multiplication
print()

# determinant of matrix
var5=np.matrix([[1,2],[3,4]])
print(var5)
print()
print(np.linalg.det(var5)) #determinant is -2




