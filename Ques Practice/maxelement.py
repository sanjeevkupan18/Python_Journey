list=[]
n=int(input("Enter the loop size :"))
for i in range(0,n):
    l=int(input("Enter the values : "))
    list.append(l)

min_elem =min(list)
max_elem=max(list)
max_positions = [index for index, value in enumerate(list) if value == max_elem]
min_positions = [index for index, value in enumerate(list) if value == min_elem]
print(list)
print(max_elem)
print(min_elem)
print(max_positions)
print(min_positions)