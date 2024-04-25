some_lst=['a','b','c','b','d','m','n','n']

dup= list(set([x for x in some_lst if some_lst.count(x) >1 ]))
print(dup)