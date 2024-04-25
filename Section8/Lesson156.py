# Create a decorator

def my_decorator(func):
    def wrap_func(*args,**kwargs): # If we wanna add a parameter to the calling function of my_decorator, should add a parameter here
        print("***************")
        func(*args,**kwargs)
        print("***************")

    return wrap_func


@my_decorator
def hello(greeting,emoji):
    print(greeting,emoji)


@my_decorator
def bye():
    print("See ya later")

hello("Hey","💛")