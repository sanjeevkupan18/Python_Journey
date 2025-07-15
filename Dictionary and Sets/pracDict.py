school={
    "Sanju":45,
    "musu":56,
    "dude":44
}

print(school.items())
print(school.popitem()) #pop out the last key value pair
school.update({"bacha":89}) #add one more key value pair
print(school)
print(school.get("Sanju")) #print the value of the desired key