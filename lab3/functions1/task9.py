import math
def volumeS(radius):
    return 4/3*math.pow(radius, 3)*math.pi

r = int(input('Enter a radius: '))
print('Volume of a given sphere = ' + str(volumeS(r)))