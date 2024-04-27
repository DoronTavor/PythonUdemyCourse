# Lesson 175- Python Built-in modules
import random

# help(random)
# print(dir(random))

print(random.random())
print(random.randint(1, 99))
print(random.choice([1, 2, 3, 4, 5, 6, 7]))
my_list=[1, 2, 3, 4, 5, 6, 7]
random.shuffle(my_list)
print(my_list)
