import re

text = "computer was expensive, but i bought it for credit."
pattern = "[,. ]"

print(re.sub(pattern, ':', text))
