import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    
    a=int(input("Guess the number :"))
    if(a>n):
        print("Lower number please")
        guesses+=1  
    elif(a<n):
        print("Greater number please")
        guesses+=1        

print(f"You guess the number {n} in {guesses+1} ways.")            