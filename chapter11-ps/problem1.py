class twovector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        
    def show (self):
        print(f"the vector is {self.i}i + {self.j}j")

class threeDvector(twovector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k 

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

a = twovector(1,2)
a.show()
b = threeDvector(1,2,3)
b.show()                       