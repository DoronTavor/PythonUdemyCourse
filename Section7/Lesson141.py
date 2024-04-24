# Pure Functions
# Rules-for the same input return the same output, and also do not affect the outside world
# For example-function with print method isn't pure
def multiply_by2(li):
    new_lst = []
    for item in li:
        new_lst.append(item * 2)
    return new_lst


print(multiply_by2([1, 2, 3]))
