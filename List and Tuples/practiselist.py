list=[]
n=int(input("Enter the size of list:"))
for i in range(0,n):
    l=int(input(f"Enter the number {i+1} :"))
    list.append(l)
print(list)
list.insert(2,56)  #at index 2 insert 56
print(list)
max_element=max(list)
print(max_element)
list.clear()
print(list)  #clears the entire list elements