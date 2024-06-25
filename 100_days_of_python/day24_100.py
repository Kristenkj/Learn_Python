import random


def roll_dice(sides):
    dice = random.randint(1, sides)
    print("You rolled", dice)
    while True:
        roll_again = input("Roll again? ")
        if roll_again.lower() == "yes":
            roll_dice(sides)
            print("You rolled ", dice)
            continue
        else:
            print("Thanks for playing!")
            exit()


roll_dice(400)
