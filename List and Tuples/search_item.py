list=[12,34,23,45,67,89,24,23]
x=int(input("Enter a number to search :"))
flag=0
for ele in list:
    if x in list:
        flag=1
    else:
        flag=0
        
if(flag==0):
    print("not found")
else:
    print("element is present")
