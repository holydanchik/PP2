def palindrome(string):
    revstring = "".join(reversed(string))
    if string == revstring:
        print("This string is palidrome")
    else:
        print("This string is not palindrome")
        
s=input('Write your string:')
palindrome(s)