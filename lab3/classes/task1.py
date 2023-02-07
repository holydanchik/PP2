class myClass:
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Enter a string: ")
    
    def printString(self):
        print(self.s.upper())

word = myClass()

word.getString()
word.printString()
