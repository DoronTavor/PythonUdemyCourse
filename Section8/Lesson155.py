# Create a decorator

def my_decorator(func):
    def wrap_func():
        print("***************")
        func()
        print("***************")

    return wrap_func


@my_decorator
def hello():
    print("Hello")


@my_decorator
def bye():
    print("See ya later")


hello()
bye()

hello2=my_decorator(hello)
hello2()
