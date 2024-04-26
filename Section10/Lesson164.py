# Generators
# range for example is a generator
# print(list(range(100)))


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_lst = make_list(100)
print(my_lst)