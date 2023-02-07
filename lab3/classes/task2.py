class Shape:
    def __init__(self):
        self.area = 0
    def getArea(self):
        return self.area
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = length * length

x = Square(int(input("Enter a length: ")))
print(x.getArea())
        