num=int(input("Enter the number :"))
a=0
b=1
c=a+b
print(a,b,end=",")
for i in range(2,num):
   
    print(c,end=",")
    a=b
    b=c
    c=a+b 