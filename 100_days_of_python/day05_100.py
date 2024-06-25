myName = input("What's your name?: ")
fly_char = input("Can you fly? ")
fast_char = input("Can you run fast? ")
strength_char = input("Can you lift heavy things? ")
stretch_char = input("Can you stretch your body really long? ")
color_char = input ("What color are you? ")
cold_char = input("Can you freeze things? ")


if fly_char == "Yes" and strength_char == "Yes":
  print(myName, "You might be Iron Man!")
if strength_char == "Yes" and color_char == "Green":
  print(myName, "You might be Hulk!")
if fly_char and strength_char == "Yes":
  print(myName, "You might be Superman!")
if cold_char == "Yes":
  print(myName, "You might be freeze ray!")
if fly_char == "No" and fast_char == "Yes":
  print(myName, "You might flash!")
if fly_char == "No" and fast_char == "No" and strength_char == "Yes":
  print(myName, "You might be Hawkeye!")

if fly_char == "No" and fast_char == "No" and strength_char == "No" and \
   strength_char == "No" and color_char != "Green" and cold_char == "No":
    print("You might be a villain!")
    