import re

def f(mObject):
    return mObject.group(1)+mObject.group(2).upper()

text = 'kbtu_is_located_in_almaty'
pattern = "([a-z])_([a-z])"

print(re.sub(pattern, f, text))