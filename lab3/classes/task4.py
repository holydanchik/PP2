import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x1, y1):
        self.x = x1
        self.y = y1
        print(f"Point ({self.x}, {self.y}) after move")
        

    def dist(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
        return math.sqrt((self.x-self.x2)**2+(self.y-self.y2)**2)
   
x = int(input("Enter a value for x-axis: "))
y = int(input("Enter a value for y-axis: "))

coordinates = Point(x, y)

coordinates.show()
print()
coordinates.move(7, 19)
print()

print('Enter coordinates of second point, to find distance')
a = int(input('value for new x: '))
b = int(input('value for new y: '))
print('Distance between points (' + str(a) + ',' + str(b) + ') and (7,19) is ' + str(coordinates.dist(a,b)))
 
    