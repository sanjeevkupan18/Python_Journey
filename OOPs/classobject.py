class employee:
    language="py"  #this is a class attribute
    salary=1000000

sanju=employee()
sanju.name= "Sanju"  #this is a instance attribute
print(sanju.name,sanju.language,sanju.salary)

rohan=employee()
rohan.name="Rohan"
print(rohan.salary,rohan.language,rohan.name)
 
# here name is object/instance attribute and salary and language is class attribute as 
# it belongs to the class