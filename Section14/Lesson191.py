# Regular Expressions
import re
pattern = re.compile('this')
my_str = 'search this inside of this text please!'

a = pattern.search(my_str) # Gives an output of an object, not just true and false, but also the indexes (start,end)
pattern2= re.compile(my_str)
print(a)
print(a.span())
print(a.start())
print(a.end())
print(a.group()) # The part of the string

b= pattern.findall(my_str)
c= pattern.fullmatch(my_str)
d= pattern2.match(my_str)
print(b)
print(c)
print(d)