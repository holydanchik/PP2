import math

class Shape():
    def __init__(self):
        self.area = 0
    def getArea(self):
        return self.area
    
class parallelogram(Shape):
    def __init__ (self, l, h):
        self.l = l
        self.h = h
        self.area = self.l * self.h 

length = float(input('Length of base: '))
height = float(input('Height of parallelogram: '))

a = parallelogram(length, height)

print('Expected output: ' + str(a.getArea()))
