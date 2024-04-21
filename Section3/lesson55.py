# Dictionary methods
user= {
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}
print(user.get('age',55))

print('basket' in user.keys())
print('age' in user.keys())


print(user.clear())
user= {
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}
user2= user.copy()
print(user2)

print(user.pop("age"))

print(user.popitem())
user.update({'age':55})
print(user)