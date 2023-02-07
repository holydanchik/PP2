numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_prime(x):
    if x<2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False    
    return True
    
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)