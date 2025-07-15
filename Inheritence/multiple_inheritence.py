class employee:
    company="Google"
    name="ramu"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class coder:
    language="Python"
    def printlang(self):
        print(f"Out of all the languages here is your language : {self.language}")

class programmer(employee,coder):
    company="Microsoft"
    def showlang(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a=employee()
b=programmer()

b.show()
b.printlang()
b.showlang()