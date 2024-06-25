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


character_1 = ' '
character_2 = ''

# this code signifies the beginning of the character creation process of the game
print("⚔️ Character Builder ⚔️")
print()
# the below code asks the user to name the character and to input a character type
c1_name = input("Name your Legend:\n ")
c1_type = input("What is your character type? Human, Elf, Wizard, Orc:\n")
# the below code concats the name and type of the character
character_1 = c1_name + " the " + c1_type
print()
# the code below prints out the name of the character and the health and strength stats
print(character_1)
c1_health = characterHealthStat()
c1_strength = characterStrengthStat()
print("STRENGTH: ", c1_strength)
print("HEALTH: ", c1_health)
print()

print("Who are thay battling?")
# the below code asks the user to name the character and to input a character type
c2_name = input("Name your Legend:\n")
c2_type = input("What is your character type? Human, Elf, Wizard, Orc:\n")
# the below code concats the name and type of the character
character_2 = c2_name + " the " + c2_type
print()
# the code below prints out the name of the character and the health and strength stats
print(character_2)
c2_strength = characterStrengthStat()
c2_health = characterHealthStat()
print("STRENGTH: ", c2_strength)
print("HEALTH: ", c2_health)
print()

round = 0
winner = None

while True:
    if c1_health <= 0:
        print(character_2, "wins!")
        winner = character_2
        break
    elif c2_health <= 0:
        print(character_1, "wins!")
        winner = character_1
        break
    else:
        print("The battle begins!")
        round += 1

    time.sleep(3)

    # This code signifies the beginning of the battle
    print("⚔️ Battle Time ⚔️")
    print()
    print("The battle begins!")
    print("Roll the highest dice to win the round!")
    # This code clears the screen before each individual battle begins
    os.system("clear")

    c1_roll = diceRolls(6)
    c2_roll = diceRolls(6)

    # This code signifies the damage done to the character
    damage = abs(c1_strength - c2_strength) + 1

    if c1_roll > c2_roll:
        c2_health -= damage
        print(character_2, "takes a hit, with ", damage, " damage")
        print("The winner of this round is", character_1)
        print()
        print(character_1, "has ", c1_health, "remaing")
        print()
        print(character_2, "has ", c2_health, "remaing")
        continue
    elif c1_roll < c2_roll:
        c1_health -= damage
        print(character_1, "takes a hit, with ", damage, " damage")
        print("The winner of this round is", character_2)
        print()
        print(character_1, "has ", c1_health, "remaing")
        print()
        print(character_2, "has ", c2_health, "remaing")
        continue
    elif c1_roll == c2_roll:
        print("It's a draw!")
        print("The winner of this round is", character_1)
        print()
        print(character_1, "has ", c1_health, "remaing")
        print()
        print(character_2, "has ", c2_health, "remaing")
        continue
    else:
        print("Something went wrong!")
        exit()

time.sleep(3)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")