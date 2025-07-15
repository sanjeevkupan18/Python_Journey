a1=int(input("enter the number :"))
a2=int(input("enter the number :"))
a3=int(input("enter the number :"))
a4=int(input("enter the number :"))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greatest.")
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greatest.")
elif(a3>a2 and a3>a1 and a1>a4):
    print("a3 is greatest.")
else:
    print("a4 is greatest.")    