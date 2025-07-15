class employee:
    company="Google"
    def show(self):
        print(f"The name of the employee is {self.company} and the salary is {self.language}")


class programmer(employee):
    company="Microsoft"
    def showlang(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a=employee()
b=programmer()

print(a.company,b.company)