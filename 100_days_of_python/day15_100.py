do_you_want_to_play = input("This is a game of animal sounds. Do you want to play?  ")
sounds_of_animals = input("What animal sound do you want to hear?  ")
animals_I_Hear = [ ]


while do_you_want_to_play == "yes":
  if sounds_of_animals.lower() == "cow":
    print("MOOOOOO")
    animals_I_Hear.append("cow")
    do_you_want_to_play = input("Do you want to play again?  ")
    if do_you_want_to_play.lower() == "no":
      print("Okay! Thanks for playing!")
  elif sounds_of_animals.lower() == "dog":
    print("Woof-Woof")
    animals_I_Hear.append("Dog")
    do_you_want_to_play = input("Do you want to play again?  ")
    if do_you_want_to_play.lower() == "no":
      print("Okay! Thanks for playing!")
  elif sounds_of_animals.lower() == "cat":
    print("Meow")
    animals_I_Hear.append("Cat")
    do_you_want_to_play = input("Do you want to play again?  ")
    if do_you_want_to_play.lower() == "no":
      print("Okay! Thanks for playing!")
  elif sounds_of_animals.lower() == "bird":
    print("Chirp-chirp")
    do_you_want_to_play = input("Do you want to play again?  ")
    if do_you_want_to_play.lower() == "no":
      print("Okay! Thanks for playing!")
  elif sounds_of_animals.lower() == "lion":
    print("Roooaaaarrrr")
    do_you_want_to_play = input("Do you want to play again?  ")
    if do_you_want_to_play.lower() == "no":
      print("Okay! Thanks for playing!")
  else:
    print(f"I don't know what sound {sounds_of_animals} makes")

