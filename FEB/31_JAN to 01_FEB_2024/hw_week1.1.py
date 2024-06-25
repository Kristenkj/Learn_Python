#Task #1 - Take a user input (name, age, roll_number, phone_number) and print the
# user details
from os import sep

print("*** Here are you details:", "\nName:",(input('Enter your name: ')), "\nAge:",(int(input('Enter your age: '))),
      "\nPhone Number:",(int(input('Enter your phone number using numbers only [No spaces or dashes]: '))),
      "\nRoll Number",(float(input('Enter your roll number: '))))

