import re

text = 'Hi.World-And Mars'
pattern = "[A-Z][a-z]+"
print(re.findall(pattern, text))