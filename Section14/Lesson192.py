# Regular Expressions
import re
my_str = 'search this inside of this text please!'
pattern = re.compile(r"([a-zA-Z]).([a])")
a = pattern.search(my_str) # Gives an output of an object, not just true and false, but also the indexes (start,end)
b= pattern.findall(my_str)
c= pattern.fullmatch(my_str)
d= pattern.match(my_str)
print(a.group())
print(a)
print(a.group(1))
