import sys
import random
FIRST,SECOND = int(sys.argv[1]),int(sys.argv[2])
num_rand= random.randint(FIRST,SECOND)
while True:
    try:
        number = int(
            input(f'Please choose a number that falls between {FIRST} to {SECOND}: '))
        if FIRST <= number <= SECOND:
            if number == num_rand:
                print("You are correct")
                break
        else:
            print(f"Enter a number in the range of {FIRST,SECOND} ")

    except ValueError:
        print("Enter a number")
        continue


