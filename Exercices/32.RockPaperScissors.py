import random
import messages
import os


def new_game():
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


def play_again():
    response = input("Would you like to play again? (Y/N): ").lower()
    if response == "y":
        return True
    elif response == "n":
        return False
    else:
        print("Enter a valid answer")
        play_again()


new_game()

while play_again():
    new_game()


messages.bye()
