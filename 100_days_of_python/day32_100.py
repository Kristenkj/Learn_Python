import random

def getChoices():
  random_greeting = random.randint(0, 5)
  greetings = ["Hello", "Bonjour", "Hola", "Zdravstvuyte", "Nǐn hǎo", "Salve"]
  return greetings[random_greeting]



print(f"The greeting is {getChoices()}")

