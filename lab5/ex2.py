import re

print(re.match(r'a[b]{2,3}', "abb"))
print(re.match(r'a[b]{2,3}', "abbb"))
print(re.match(r'a[b]{2,3}', "ab"))
print(re.match(r'a[b]{2,3}', "ac"))

