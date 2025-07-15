import numpy as np 

#using where function for searching
var=np.array([1,2,3,4,5,6,7,8,9])
x=np.where((var%2)==0)
print(x)
print()

#search sorted function finds the index of the elements whom we are searching
var1=np.array([1,2,3,4,6,7,8,9])
x1=np.searchsorted(var1,5) #tells that 5 is placed at index 4 in this sorted array
print(x1)
print()

#search sorting by right side
var2=np.array([1,2,3,4,9])
x2=np.searchsorted(var2,[5,6,7,8]) #tells that these number must be placed at index 4
print(x2) 
print()

# sort (ascending or descending)
var3=np.array([2,6,5,7,9,23,78,1,3]) #we can sort string also
print(np.sort(var3))
print()

#sorrting 2 Dimension array
var4=np.array([[23,12,1],[56,22,31]])
print(np.sort(var4))
print()

# Filter function
var5=np.array(["a","s","d","f"])
f=[True,False,True,False]
newarray=var5[f] #create new array with filtered elements
print(newarray)
print()