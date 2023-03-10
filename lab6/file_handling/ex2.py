import os

path = "E:\\test\\good.txt"

if os.path.exists(path):
    print("It does exist")
    
    with open(path, "r") as f:
        print("\nThis file is readable") if f.readable() else print("\nThis file is NOT readable")
    
    with open(path, "w") as f:
        print("\nThis file is writable") if f.writable else print("This file is NOT writable")
            
    print("\nThis file is executable") if os.access(path, os.X_OK) else print("\nThis file is NOT executable")
else:
    print("It does not exist")
    

    

    
