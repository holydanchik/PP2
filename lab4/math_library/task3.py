from math import tan, pi

class Shape():
    def __init__(self):
        self.area = 0
    
    def getArea(self):
        return self.area
    
class polygon(Shape):
    def __init__(self, s, l):
        self.s = s
        self.l = l
        self.area = self.s * (self.l**2) / (4*tan(pi/self.s))

sides = int(input('Input number of sides: '))
length = float(input('Input the length of a side: '))

a = polygon(sides, length)
print('The area of a polygon is: ' + str(int(a.getArea())))

