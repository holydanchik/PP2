import re

text = "HelloWorldAndMars"
pattern = "[A-Z][^A-Z]*"

print(re.findall(pattern, text))

# or

print(re.split(r'(?=[A-Z])', text))

