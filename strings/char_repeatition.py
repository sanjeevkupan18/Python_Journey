# str=input("Enter the string :")

# res=[]

# for i in set(str):
#     if(str.count(i)>1):
        
        
#         res.append(i)
#     else:
#         -1

# print(res)


string = "Welcome to TutorialsPoint family"
print("All the duplicate characters in the string are: "); 
# Counting every characters of the string 
for s in range(0, len(string)): 
   count = 1; 
   for t in range(s+1, len(string)):
      if(string[s] == string[t] and string[s] != ' '): 
         count = count + 1; 
# setting the string t to 0 to avoid printing the characters already taken 
   #string = string[:t] + '0' + string[t+1:]; 
# If the count is greater than 1, the character is considered as duplicate 
   if(count > 1 and string[s] != '0'): 
      print(string[s]," - ",count)

      