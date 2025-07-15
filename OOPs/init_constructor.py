class employee:
    language="py"  #this is a class attribute
    salary=1000000

    def __init__(self,name,salary,language): #init is a dunder function which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creating an object")

harry=employee("harry",130000,"java")  #providing 3 argument values  
print(harry.name,harry.salary,harry.language)    


