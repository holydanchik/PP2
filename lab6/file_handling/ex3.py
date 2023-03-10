import os

path = "E:\\test\\good.txt"

if os.path.exists(path):
    print("File name of the path: " + os.path.basename(path))
    print("Dir name of the path: " + os.path.dirname(path))
else:
    print("Does not exist")