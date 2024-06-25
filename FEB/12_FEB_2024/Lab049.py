"""
Factorial
n = 5
5 * 4* 3 * 2 * 1 = 120

Factorial of zero is not possible
"""

number = int(input("Enter the factorial number:  \n"))

if number < 0:  # This makes sure the factorial is < 0; because factorial < 0 isn't possible
    print("This number doesn't qualify as a factorial because it is less than zero.")
elif number == 0:
    print("The factorial of zero is  ", 1)
else:
    factorial = 1  # This number determines the consistency of the factorial.. wether it goes by 1s or 2s
    for i in range(1, number + 1):  # starts at 1 and adds to it
        factorial = factorial * i

    print("The factorial is  ", factorial)
