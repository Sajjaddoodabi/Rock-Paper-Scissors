import random

print("Rock...")
print("Paper...")
print("Scissors...")
print("------------------------------")
Moves = ["rock", "paper", "scissors"]

winning_point = 4

player1_wins = 0
CMD_wins = 0

print("tip : you can quit the game whenever you want by typing 'q' in the chat!")
print("------------------------------")

while player1_wins < winning_point and CMD_wins < winning_point :
    print(f"player1 : {player1_wins} | CMD : {CMD_wins}")
    Player1 = input("player1 make your move : ").lower()
    CMD = random.choice(Moves)
    print(f"CMD make your move : {CMD}")

    if Player1 == "q":
        print()
        break

    if Player1 == CMD:
        print("that's a tie! \n")

    elif Player1 == "rock":
        if CMD == "paper":
            print("you lost! \n")
            CMD_wins += 1
        elif CMD == "scissors":
            print("you win! \n")
            player1_wins += 1
    elif Player1 == "paper":
        if CMD == "rock":
            print("you win! \n")
            player1_wins += 1
        elif CMD == "scissors":
            print("you lost! \n")
            CMD_wins += 1
    elif Player1 == "scissors":
        if CMD == "paper":
            print(" you win! \n")
            player1_wins += 1
        elif CMD == "rock":
            print("you lost! \n")
            CMD_wins += 1
    else:
        print("something went wrong! \n")


print(f"Final score : player1 : {player1_wins} | CMD : {CMD_wins}")
if player1_wins == winning_point :
    print("YOU ARE THE WINNER!")
elif CMD_wins == winning_point :
    print("YOU LOST!")


