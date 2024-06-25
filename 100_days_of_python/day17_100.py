from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")
print()
print("R= Rock, P= Paper, S= Scissors")
print()
print(
    "There are two players, each player will choose one of the three options,"
    " and the winner will be decided by the rules below:")
print()

player_1 = input("Player 1, select your move (R, P or S): ")
player_2 = input("Player 2, select your move (R, P or S): ")

p2_score = 0
p1_score = 0

while True:
    if p2_score == 0 and p1_score == 0:
        print("Let the games begin!")
        print()
    elif (p2_score < 3 and p2_score > 0) and (p1_score < 3 and p1_score > 0):
        print("The game continues!")
        print()
    elif p2_score == 3 or p1_score == 3:
        print("The game is over!")
        print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
        exit()

    if player_1 in ["R", "r", "Rock", "rock"]:
        if player_2 in ["R", "r", "Rock", "rock"]:
            print("You both picked Rock, draw!")
            if p2_score == 3 or p1_score == 3:
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
        elif player_2 in ["S", "s", "scissors", "Scissors"]:
            print("P1 smashed P2's Scissors into dust with their Rock!")
            print("One point to P1!")
            p1_score += 1
            if p2_score == 3 or p1_score == 3:
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
        elif player_2 in ["P", "p", "paper", "Paper"]:
            print("P2's Paper wraps around P1's Rock!")
            print("One point to P2!")
            p2_score += 1
            if p2_score == 3 or p1_score == 3:
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
        else:
            print("Invalid move, try again")
            if p2_score == 3 or p1_score == 3:
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
    elif player_1 in ["P", "p", "paper", "Paper"]:
        if player_2 in ["R", "r", "Rock", "rock"]:
            print("P1's Paper wraps around P2's Rock!")
            print("One point to P1!")
            p1_score += 1
            if p2_score == 3 or p1_score == 3:
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
        elif player_2 in ["S", "s", "scissors", "Scissors"]:
            print("P2's Scissors cuts P1's Paper into pieces!")
            print("One point to P2!")
            p2_score += 1
            if p2_score == 3 or p1_score == 3:
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
        elif player_2 in ["P", "p", "paper", "Paper"]:
            print("You both picked Paper, draw!")
            if p2_score == 3 or p1_score == 3:
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
        else:
            print("Invalid move, try again")
            if p2_score == 3 or p1_score == 3:
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
    elif player_1 in ["S", "s", "scissors", "Scissors"]:
        if player_2 in ["R", "r", "Rock", "rock"]:
            p2_score += 1
            print("P2's Rock smashes P1's Scissors into dust with their Rock!")
            print("One point to P2!")
            if (p2_score == 3) or (p1_score == 3):
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
        elif player_2 in ["S", "s", "scissors", "Scissors"]:
            print("You both picked Scissors, draw!")
            if (p2_score == 3) or (p1_score == 3):
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
        elif player_2 in ["P", "p", "paper", "Paper"]:
            p1_score += 1
            print("P1's Scissors cuts P2's Paper into pieces!")
            print("One point to P1!")
            if ((p2_score == 3) or (p1_score == 3)):
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif ((p1_score != 3) or (p2_score != 3)):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
        else:
            print("Invalid move, try again")
            if (p2_score == 3) or (p1_score == 3):
                print("The game is over!")
                print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
                exit()
            elif (p1_score != 3) or (p2_score != 3):
                print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
                continue
    else:
        print("Invalid move, try again!")
        if (p2_score == 3) or (p1_score == 3):
            print("The game is over!")
            print("The final score is: Player 1:", p1_score, "Player 2:", p2_score)
            exit()
        elif (p1_score != 3) or (p2_score != 3):
            print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points")
            continue

