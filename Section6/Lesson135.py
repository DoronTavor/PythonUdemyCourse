# DUNDER METHODS-methods with __nameOfMethod__
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict={
            "Name":"Bonzie",
            "has_pets":False
        }

    def __str__(self):  # Override the Dunder method of __str__
        return f"{self.color}"

    def __len__(self):  # Override the Dunder method of __len__
        return 5

    def __del__(self):  # Override the Dunder method of __del__
        print("deleted")

    def __call__(self, *args, **kwargs): # Override the Dunder method of __call__
        return "Yesss?"

    def __getitem__(self, i): # Override the Dunder method of __getitem__
        return self.my_dict[i]

action_figure = Toy("Yellow", 0)
print(action_figure.__str__())  # Gets <__main__.Toy object at 0x000001C41FE6D030> if not overriding it
# Same as: str(action_figure)

# We can customize the dunder methods
print(len(action_figure))
print(action_figure())
print(action_figure['Name'])
del action_figure

