def palindrome(word):
    pal = word[::-1]
    if pal==word:
        print(word, "is a palindrome")
    else:
        print(word, 'is not a palindrome')

s = input('Enter a word: ')
palindrome(s)