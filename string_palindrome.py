def isPalindrome(s):
    return s[ : :-1]

s=input()
# ans=isPalindrome(s)
# if(ans==s):
#     print("String palindrome")
# else:
#     print("NOT")
print(isPalindrome(s))