def solve(h, l):
    rabbit = int((l - 2*h) / 2)
    chicken = h - rabbit
    print("There are " + str(chicken) + " chickens and " + str(rabbit) + " rabbits")
    
    
heads = int(input("Enter number of heads: "))
legs = int(input("Enter number of legs: "))
solve(heads, legs)


# 2x + 2y = 2 heads 
# 2x + 4y = legs
# rabbit = (legs - 2 heads) / 2