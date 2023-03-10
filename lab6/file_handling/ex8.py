import os

path = "C:\\Users\\tuzel\\OneDrive\\Рабочий стол\\knockout.txt"
if not os.path.exists(path):
    open(path, 'x')


print(os.path.exists(path)) 
os.remove(path)