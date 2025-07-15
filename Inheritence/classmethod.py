class employee:
    a=1

    @classmethod #show the class attribute instead of 45
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

e=employee()
e.a=45
e.show()      