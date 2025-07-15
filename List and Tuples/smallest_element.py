list=[]
n=int(input("Enter the size of list:"))
for i in range(0,n):
    l=int(input(f"Enter the number {i+1} :"))
    list.append(l)
list.sort()
print(list[0])