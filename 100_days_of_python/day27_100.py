import random
import os, time


def diceRolls(sides):
    dice_size = random.randint(1, sides)
    return dice_size


# function that multiplies a bunch of random dice rolls together to generate the character health stats

def characterHealthStat():
    health_stat = diceRolls(6) * diceRolls(12) / 2 + 10
    return health_stat


# function that multiplies a bunch of random dice rolls together to generate the character strength stats

def characterStrengthStat():
    strength_stat = diceRolls(6) * diceRolls(12) / 2 + 12
    return strength_stat


while True:
    os.system('clear')
    print("⚔️ Character Builder ⚔️")
    time.sleep(1)
    print()
    name = input("Name your Legend:\n")
    type = input("Character Type (Human, Elf, Wizard, Orc):\n")
    print()
    print(name+ " the "+ type)
    print("STRENGTH: ", characterStrengthStat())
    print("HEALTH: ", characterHealthStat())
    print()
    time.sleep(1)
    print("May your name go down in Legend...")
    time.sleep(1)
    menu = input("Would you like to create another character? ")
    if menu.lower() == "yes":
        continue
    else:
        exit()
