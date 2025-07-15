num1=int(input("Enter the number 1 :"))
num2=int(input("Enter the number 2 :"))
if(num1>num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
else:
    num2=num2-num1
    num1=num1+num2
    num2=num1-num2
print(f"After swapping number 1 : {num1} and number 2 : {num2}")        