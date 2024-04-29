import random
FIRST,SECOND = 1,10

def run_guess(guess,answer):
    if FIRST <= guess <= SECOND:
        if guess == answer:
            print("You are correct")
            return True
        else:
            return False
    else:
        print(f"Enter a number in the range of {FIRST, SECOND} ")
        return False
if __name__ == '__main__':

    num_rand= random.randint(FIRST,SECOND)
    while True:
        try:
            number = int(
                input(f'Please choose a number that falls between {FIRST} to {SECOND}: '))
            if(run_guess(number,num_rand)):
                break


        except ValueError:
            print("Enter a number")
            continue


