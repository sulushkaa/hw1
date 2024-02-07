def Palindrome(word):
    reverse = word[::-1]
    if reverse == word :
       return True
    else:
        return False

string = input("Enter your string:")
if Palindrome(string) :
    print("Yes, it is a palindrome")
else: 
    print("No, it's not a palindrome")