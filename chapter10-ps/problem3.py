class demo:
    a=4

o=demo()
print(o.a) #prints the class attribute coz instance attribute is not present
o.a=0     #now instance attribute is set
print(o.a)    #prints the instance attribute coz instance attribute is pressent
print(demo.a)  #prints the class attribute

#hence the value of class attribute does not changes.