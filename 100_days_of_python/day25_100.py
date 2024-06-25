
import random


def roll_dice(sides):
    dice_size = random.randint(1, sides)
    return dice_size


def char_health_stat():
    roll_6_sided_dice = roll_dice(6)
    roll_8_sided_dice = roll_dice(8)
    health_stat = roll_6_sided_dice * roll_8_sided_dice
    return health_stat


print("⚔️Character stats generator⚔️")

change_warrior = "yes"

health_stat = char_health_stat()
while change_warrior == 'yes':
    warrior_name = input("What is your warrior's name? ")
    health_stat = char_health_stat()
    print(f"Your warrior's name is {warrior_name} and their health is {health_stat}")
    change_warrior = input("Do you want to create a new character? ")

