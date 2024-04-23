# FUNCTIONS- a combination of multiple lessons

# Functions without parameters
def say_hello():
    print("HELLLLLLO")

# Functions with parameters
def calculate_power(x, y):
    print(f"The result of {x} power by {y} is {x ** y}")
def say_hello_to(name,emo):
    print(f"hello to {name}, {emo*7}")

# Default parameters
def say_default(emo="💙",name="Milson"):
    print(f"hello {name} the king {emo*10}")

# Functions with return
def sum_nums(num1,num2):
    return num1+num2

def mul_nums(num1,num2):
    def another(n1,n2):
        return n1*n2
    return another(num1,num2)
calculate_power(2, 5)
say_hello()
say_hello_to("tavor","💛")
say_default()
print(sum_nums(1,2))
print(mul_nums(20,30))