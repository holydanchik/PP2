class Shape():
    def __init__(self):
        self.area = 0
    
    def getArea(self):
        return self.area

class trapezoid(Shape):
    def __init__(self, h, a, b):
        self.h = h
        self.a = a
        self.b = b
        self.area = (self.b + self.a)*0.5*self.h

height = float(input('Height: '))
base1 = float(input('Base, first value: '))
base2 = float(input('Base, second value: '))

area = trapezoid(height, base1, base2)
print('Expected output: ' + str(area.getArea()))
