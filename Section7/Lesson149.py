# List Comprehensions
my_list= [char for char in 'hello']
print(my_list)

my_lst2= [num for num in range(0,100)]
print(my_lst2)

my_lst3= [num *2 for num in range(0,100)]
print(my_lst3)

my_lst4= list(filter(lambda item: item % 2 != 0, [num **2 for num in range(0,100)]))
print(my_lst4)