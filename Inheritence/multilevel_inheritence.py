class employee:
    a=1

class programmer(employee):
    b=2

class manager(programmer):
    c=3

o=employee()
print(o.a) #print the a attribute
#print(o.b)  ##shows an error as there is no attribute in employee class

o=programmer()
print(o.b,o.a)

o=manager()
print(o.c,o.b,o.a)