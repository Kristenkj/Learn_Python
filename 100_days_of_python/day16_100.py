name = input("What is your name? ")


while True:
  fill_in_the_lyrics = input("What's the missing word in the lyrics? 'Never going to ______ you up.' ")
  if fill_in_the_lyrics == "give":
    print(f"Well done {name}")
    break
  else:
    print(f"Sorry, {name}, try again.")