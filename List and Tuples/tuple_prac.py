list=[]

n=int(input("Enter the number :"))
for i in range(0,n):
    t=int(input(f"Enter the value {i+1} :"))
    list.append(t)
tuple=tuple(list)   #converting list into tuple as tuple are immutable 
print(tuple)  
print(type(tuple))  