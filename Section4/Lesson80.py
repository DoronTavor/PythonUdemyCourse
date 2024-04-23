some_list= ["a","b","c","b","d","m","n","n"]

dup = []
for i in some_list:
    if some_list.count(i)>1 and i not in dup:
        dup.append(i)

print(dup)