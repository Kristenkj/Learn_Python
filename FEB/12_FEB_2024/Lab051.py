"""
Match Case is similar to switch case in JAVA
 Match doesn't use break. It automatically happens.
"""

numbers = int(input("Enter a number\n"))
match numbers:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case _:                             #This is default case
        print("No idea")
