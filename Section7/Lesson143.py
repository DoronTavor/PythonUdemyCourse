# filter()
def check_if_odd(item):
    return item % 2 !=0

print(list(filter(check_if_odd,[1,2,3])))