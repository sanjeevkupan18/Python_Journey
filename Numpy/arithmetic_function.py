import numpy as np 

var=np.array([1,2,3,4,5,7,8])
print(f"minimum :{np.min(var)},{np.argmin(var)}")
print(f"maximum :{np.max(var)},{np.argmax(var)}")
print(f"square root : {np.sqrt(var)}")
print("\n")

var1=np.array([[1,2,3,4],[2,3,4,5]]) #2Dimension
print(np.min(var1,axis=0)) #axis=0 for column operation and axis=1 for row operation
print()

x=np.array([1,2,3])
print(np.sin(x))
print(np.cos(x))
print(np.cumsum(x))