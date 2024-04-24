# set and dictionary Comprehensions
my_list= {char for char in 'hello'}
print(my_list)

my_lst2= {num for num in range(0,100)}
print(my_lst2)

my_lst3= {num *2 for num in range(0,100)}
print(my_lst3)

my_lst4= set(filter(lambda item: item % 2 != 0, {num **2 for num in range(0,100)}))
print(my_lst4)

simple_dict={
    'a':1,
    'b':2
}
my_dict={key:value**2 for key,value in simple_dict.items() if value %2 ==0}
print(my_dict)

my_new_dict= {num: num*2 for num in [1,2,3]}
print(my_new_dict)