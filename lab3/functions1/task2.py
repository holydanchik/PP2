def to_centigrade(n):
    return 5/9*(n-32)

f = int(input("Enter a temperature in Fahrenhite: "))
print(to_centigrade(f))