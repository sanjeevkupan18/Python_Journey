class animal:
    pass
class pets(animal):
    pass
class dogs(pets):
    @staticmethod
    def bark():
        print("wow wow!!")
a=dogs()
a.bark()        