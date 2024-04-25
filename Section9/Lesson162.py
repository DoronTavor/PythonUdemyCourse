# Error handling
while True:

    try:
        age = int(input("What is your age? "))
        new_age= age/10
        print(age)


    except ValueError:
        print("Please enter a number")

    except ZeroDivisionError:
        print("Please enter an age higher than zero")
    else:
        print("Thank you")
        break
    finally:
        print('Ok, i am finally done')

