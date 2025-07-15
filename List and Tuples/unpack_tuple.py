# Python3 code to study about
# unpacking python tuple using *

# first and last will be assigned to x and z
# remaining will be assigned to y
x, *y, z = (10, "Geeks ", " for ", "Geeks ", 50)

# print details
print(x)
print(y)
print(z)

# first and second will be assigned to x and y
# remaining will be assigned to z
x, y, *z = (10, "Geeks ", " for ", "Geeks ", 50)
print(x)
print(y)
print(z)
