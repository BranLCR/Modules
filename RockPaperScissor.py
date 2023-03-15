import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper, or scissor(s?: ").lower()

    print("Player: " + player)
    print("Computer: " + computer)

    if player == computer:
        print("It is a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!")
        elif computer == "paper":
            print("Computer Wins!")
    elif player == "scissors":
        if computer == "paper":
            print("Player wins!")
        elif computer == "Rock":
            print("Computer wins!")
    elif player == "paper":
        if computer == "rock":
            print("Player wins!")
        elif computer == "scissors":
            print("Computer wins!")

    play_again = input("Play again? (yes/no): ")
    if play_again != "yes":
        break
print("Thank you for playing")