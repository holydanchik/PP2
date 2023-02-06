def filter_prime(primes):
    for x in primes:
        kkk = True
        for i in range(2, int(x/2)+1):
            if x%i==0:
                kkk = False
                break
        if kkk == True:
            print(x, end=" ")
    
    
mylist = [2, 3, 4, 7, 9, 99, 345, 66, 59]
filter_prime(mylist)
