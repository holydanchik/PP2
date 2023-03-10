def function(string):
    lowers = 0
    uppers = 0
    for i in range(len(string)):
        if string[i].islower():
            lowers += 1
        elif string[i].isupper():
            uppers += 1
    print(f"Lower letters: {lowers}")
    print(f"Upper letters: {uppers}")

s=input('Write your string:')
function(s)