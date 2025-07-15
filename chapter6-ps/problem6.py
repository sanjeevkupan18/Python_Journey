marks=int(input("Enter your marks :"))

if(100>=marks and marks>=90):
    grade="Ex"
if(90>=marks and marks>=80):
    grade="A"
if(80>=marks and marks>=70):
    grade="B"
if(70>=marks and marks>=60):
    grade="C"
if(60>=marks and marks>=50):
    grade="D"
if(50>=marks):
    grade="F"

print("your grade is :",grade)    