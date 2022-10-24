import random
#implement a do-while loop in python

# create a guessing game

ran_num = random.randrange(1, 10)

while True:
    try:

        guess = int(input("Enter a number betweem 1-10: "))

        if guess == ran_num:
            print("You guessed it!")
            break
    except ValueError:
        print("Kindly enter a valid number")

    except:
        print("Unknown error occured")
