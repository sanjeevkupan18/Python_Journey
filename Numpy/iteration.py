import numpy as np 
#Using for loop
var=np.array([1,2,3,4,5,6,7])
print(var)
print()
for i in var:
    print(i)
print()    

#2 Dimension
var2=np.array([[1,2,3],[4,5,6]])
for i in var2:
    for j in i:
        print(j)
print()

#3 Dimension
var3=np.array([[[9,8,7,6],[1,2,3,4]]])
for i in var3:
    for j in i:
        for k in j:
            print(k)
print()            


# nditer functoion for iteration
var4=np.array([1,2,3,4,5,6,7,8,9])
for i in np.nditer(var4):
    print(i)
print()    

# ndenumerate function for iterating with index
var5=np.array([[[9,8,7,6],[1,2,3,4]]])
for i,d in np.ndenumerate(var5):
    print(i,d)
print()