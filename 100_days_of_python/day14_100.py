from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")
print()
print("R= Rock, P= Paper, S= Scissors")
print()
print("There will be three rounds")
print()
player_1 = input("Player 1, select your move (R, P or S): ")
print()
player_2 = input("Player 2, select your move (R, P or S): ")
print()


if player_1 in ["R","r", "Rock", "rock"]:
  if player_2 in ["R","r", "Rock", "rock"]:
    print("You both picked Rock, draw!")
  elif player_2 in ["S", "s", "scissors", "Scissors"]:
    print("P1 smashed P2's Scissors into dust with their Rock!")
  elif player_2 in ["P", "p", "paper", "Paper"]:
    print("P2's Paper wraps around P1's Rock!")
  else:
    print("Invalid move, try again")
elif player_1 in ["P", "p", "paper", "Paper"]:
  if player_2 in ["R","r", "Rock", "rock"]:
    print("P1's Paper wraps around P2's Rock!")
  elif player_2 in ["S", "s", "scissors", "Scissors"]:
    print("P2's Scissors cuts P1's Paper into pieces!")
  elif player_2 in ["P", "p", "paper", "Paper"]:
    print("You both picked Paper, draw!")
  else:
    print("Invalid move, try again")
elif player_1 in ["S", "s", "scissors", "Scissors"]:
  print("P1's Scissors cuts P2's Paper into pieces!")
  if player_2 in ["R","r", "Rock", "rock"]:
    print( "P2's Rock smashes P1's Scissors into dust with their Rock!")
  elif player_2 in ["S", "s", "scissors", "Scissors"]:
    print("You both picked Scissors, draw!")
  elif player_2 in ["P", "p", "paper", "Paper"]:
    print("P1's Scissors cuts P2's Paper into pieces!")
  else:
    print("Invalid move, try again")
else:
  print("Invalid move, try again!")
