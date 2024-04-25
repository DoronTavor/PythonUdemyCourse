
def my_sum(num1,num2):
    try:
        return num1/num2
    except (TypeError,ZeroDivisionError) as err:
        return f"Please enter numbers, and not divide by zero \n{err}"

print(my_sum(2,0))