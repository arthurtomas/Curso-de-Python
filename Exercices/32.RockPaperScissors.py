import random
import messages
import os

while True:

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if computer == player:
        print(f"Computer: {computer}")
        print(f"Player: {player}")
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You Lose!")
        elif computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You Lose!")
        elif computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You Lose!")
        elif computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You win!")

    play_again = input("Would you like to play again? (Y/N): ").lower()
    if play_again != "y":
        break

messages.bye()
