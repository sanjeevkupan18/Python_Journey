import numpy as np 
list=[]                #first we make a list then convert it into array
for i in range(0,5):
    l=int(input(f"Enter the value {i+1} :"))
    list.append(l)
y=np.array(list)
print(type(y))
print(y)   
print(y.ndim)   #print the dimension of array 