import numpy as np 
import random

var1=np.random.rand(4) #rand function gives random 4 value between 0 and 1
print(var1) 
print("\n")

var2=np.random.rand(2,3) #2row and 3column
print(var2)
print("\n")

var3=np.random.randn(4) #randn func gives close to 0 including +ve and -ve numbers
print(var3)
print("\n")

var4=np.random.ranf(4) #ranf func give range between including 0 but less than 1
print(var4)
print("\n")

var5=np.random.randint(1,20,5) #print random numbers between 1 to 20 having 5 elements
print(var5)