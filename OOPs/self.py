class employee:
    language="py"  #this is a class attribute
    salary=1000000

    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")

    @staticmethod   #marked function as static which does not take self
    def greet():
        print("Good Morning")    

sanju=employee()
sanju.language= "javascript"  #this is a instance attribute
sanju.getinfo()  #employee.getinfo(sanju)  therefore it takes one argument
sanju.greet()