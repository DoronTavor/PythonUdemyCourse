from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = "Hello world thinking about python"
print(Counter(li))
print(Counter(sentence))

dictio = defaultdict(lambda: 'Does not exist',{'a': 1, 'b': 2})
print(dictio['c'])

new_dict= OrderedDict()
new_dict['a']=1
new_dict['b']=2
new_dict2= OrderedDict()
new_dict2['b']=2
new_dict2['a']=1
print(new_dict==new_dict2)
