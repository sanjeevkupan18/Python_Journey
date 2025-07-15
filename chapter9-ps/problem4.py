word ="donkey"

with open("file.txt","r")as f:
    content=f.read()

contentnew = content.replace("donkey","######")

with open("file.txt","w") as f:
    content=f.write(contentnew)