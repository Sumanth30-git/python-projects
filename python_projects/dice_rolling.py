import random 
def dice_rolling():
    print("Welcome to the dice rolling game!")
    while True:
        input("press enter to roll the dice")
        dice = random.randint(1,6)
        print(f"you rolled a {dice}!")
        play_again = input("do you want to play again? (y/n)")
        if play_again.lower() != "y":
            print("Thanks for playing!")
            break
dice_rolling()