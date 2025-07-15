marks={
    "sanu":67,
    "manu":78,
    "janu":54,
    "list":{34,54,53}
}

print(marks,type(marks))
print(marks["sanu"])
print(marks.keys())
print(marks.values())

marks.update({"sanu":100})
print(marks)

print(marks.get("sanu2")) #prints none
print(marks["sanu2"]) #returns an error