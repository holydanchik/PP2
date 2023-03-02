import re

text = "timka_erakai danchik_ansar forrest.gump"
pattern = r'[a-z]+_[a-z]+'

print(re.findall(pattern, text))

