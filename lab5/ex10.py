import re

def f(mObject): # wmatchObject
    return mObject.group('g1')+'_'+mObject.group('g2').lower()

text = "mySuperVarKarLarB" #camelcase
pattern = "(?P<g1>[a-z])(?P<g2>[A-Z])+"

res = re.search(pattern, text)

print(re.sub(pattern, f, text))