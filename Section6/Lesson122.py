#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Joe",5)
cat2 = Cat("Bon",4)
cat3 = Cat("Alex",6)



# 2 Create a function that finds the oldest cat
def oldestCat(*args):
    return max(*args)



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
cats_age= (cat1.age,cat2.age,cat3.age)
print(f"The oldest cat is {oldestCat(cats_age)} years old")