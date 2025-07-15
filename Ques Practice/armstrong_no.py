num=int(input("Enter the number :"))
p=0
temp=num
while(num>0):
    rem=num%10
    p=p+(rem*rem*rem)
    num=num//10

if(temp==p):
    print("Yes , it is an armstrong number .")
else:
    print("No , it is not an armstrong number .")    