import random

correct_number = random.randint(1, 1000000)
guess_attempts = 0
number_guess = ''

for guess_attempts in range(5):
    number_guess = int(input("Guess a number between 0 and 1,000,000: "))
    if number_guess < 0:
        print("You have crashed the program. Now we will never know the number.")
        exit()
    elif number_guess < correct_number:
        print("Too low, try again")
        guess_attempts += 1
        if guess_attempts == 5:
            print(f"You have run out of guesses. The correct number was {correct_number}.")
    elif number_guess > correct_number:
        print("Too high, try again")
        guess_attempts += 1
        if guess_attempts == 5:
            print(f"You have run out of guesses. The correct number was {correct_number}.")
    elif number_guess == correct_number:
        print("You guessed the correct number!")
        guess_attempts += 1
        print("It took you", guess_attempts, "guesses to get the correct answer")
        break
    else:
        print("That is not a number I recognize.")



