import random

class train:
    def __init__(self,trainno):
        self.trainno=trainno
    def book(self , fro ,to):
        print(f"Ticket is booked in Train no : {self.trainno} from {fro} to {to}")

    def bookstatus(self):
        print(f"Train no : {self.trainno} is running on time ")

    def getfare(self,fro,to):
        print(f"Ticekt fare from {fro} to {to} is {random.randint(200,5000)}")

t=train(22387)
t.book("Durgapur","Dhanbad")
t.bookstatus()
t.getfare("Durgapur","Dhanbad")                     
        