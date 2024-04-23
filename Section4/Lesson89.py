# *args
def super_func(*args):
    total = 0
    for items in args:
        total+=items
    return total

print(super_func(1,2,3,4,5))

def mul_func(**kwargs):
    total = 1
    for items in kwargs.values():
        total = total* items
    return total

print(mul_func(num1=1,num2=2,num3=3,num4=4,num5=5))