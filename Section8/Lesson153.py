# Decorators-Also 154
# Look like @name

def hello(func):
    func()


def greet():
    print("Still here")


a= hello(greet)
print(a)

# Lesson 154

#Higher order function
def greet2(func):
    func()

def greet3():
    def func5():
        return 5
    return func5