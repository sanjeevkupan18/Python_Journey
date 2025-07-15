import math
def prime(n):
    
    if(n>1):
        for i in range(2,(n//2)+1):
            if(n%i==0):
                return False
            else:
                return True
    else:
        return False

x,y=map(int,input("Enter the values of x and y :").split())
if(prime(x)==True and prime(y)==True and abs(x-y)==2):
    print("TwinPrime")
else:
    print("Not twinprime")