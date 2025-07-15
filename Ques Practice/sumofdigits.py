num=int(input("Enter the number :"))
sum=0
while(num>0):
    z=num%10
    sum=sum+z
    num=num//10
print(sum)