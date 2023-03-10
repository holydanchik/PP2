import time, math

def decode(number,miliseconds):
    time.sleep(miliseconds/1000)
    print(f"Square root of {number} after {miliseconds} is {math.sqrt(number)}")
    
n = int(input())
ms = int(input())
decode(n, ms)