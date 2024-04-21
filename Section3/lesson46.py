# List Methods
basket = [1,2,3,4,5]
print(len(basket))

basket.append(100)
print(basket)
basket.insert(4,200)
print(basket)

basket.extend([100,101])
print(basket)

# REMOVING
basket.pop()
print(basket)
basket.pop(0)
print(basket)
basket.remove(200)
print(basket)


