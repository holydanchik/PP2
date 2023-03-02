import re

print(re.match(r'a[b]*', "abb"))
print(re.match(r'a[b]*', "ab"))
print(re.match(r'a[b]*', "ac"))
print(re.match(r'a[b]*', "a"))



