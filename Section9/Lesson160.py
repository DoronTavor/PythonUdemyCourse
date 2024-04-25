# Error handling
while True:

    try:
        age = int(input("What is your age? "))
        print(10/age)


    except ValueError:
        print("Please enter a number")

    except ZeroDivisionError:
        print("Please enter an age higher than zero")
    else:
        print("Thank you")
        break

