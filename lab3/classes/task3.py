class Shape:
    def __init__(self):
        self.area = 0
    def getArea(self):
        return self.area
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area_r(self):
        return self.length*self.width


a = int(input('Enter a length of rectangle: '))
b = int(input('Enter a width of rectangle: '))     
x = Rectangle(a,b)
print('The area of a given rectangle is ' + str(Rectangle.area_r(x)))