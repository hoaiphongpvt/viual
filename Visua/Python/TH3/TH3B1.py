import re
from traceback import print_tb


s = "pythonfile.py"

print(s[2])
print(s[-1])
print(len(s))
print(s[0:7])

e = s[6:10]
print(e)

f = s[10:15]
print(f)

convert = ''
for i in s[::-1]:
    convert = convert + i
print(convert)

print(s[::-1])