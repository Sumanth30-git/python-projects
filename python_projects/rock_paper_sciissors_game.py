import random
def rock_paper_scissors_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice=random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    if user_choice == computer_choice:
        print("it's Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print(f"computer choose: {computer_choice}")
        print("congratualtios \n You Win!")
    else:
        print(f"computer choose:{computer_choice}")
        print("You Lose! \n Better luck next time.")
print("welcome to rock paper scissors game")
input("press enter to play ")
rock_paper_scissors_game()
        