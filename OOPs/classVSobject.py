class employee:
    language="py"  #this is a class attribute
    salary=1000000

    

sanju=employee()
sanju.language= "javascript"  #this is a instance attribute
print(sanju.language,sanju.salary)
#instance attribute take more preference than class attribute
