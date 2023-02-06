def reverseWord(s):
    s += ' '
    mylist = []
    word = ""
    for i in s:
        if i == ' ':
            mylist.append(word)
            word = ""
        else:
            word += i
    mylist.reverse()
    for x in mylist:
        print(x, end=' ')
            
            

s = input('Enter a word: ')
reverseWord(s)