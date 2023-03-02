import re

text = 'kamkb'
pattern = "a.*b$"

print(re.findall(pattern, text))