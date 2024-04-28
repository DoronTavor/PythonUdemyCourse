# Password checker
# the password should be: At least 8 char long, contain any sort letter, numbers $%#@
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
import re
regex = r"[a-zA-Z0-9$#%@]{8,}\d"
pattern = re.compile(regex)
string = 'Tadoron123456'

a = pattern.search(string)
check= pattern.fullmatch(string)
print(check)


