import random
def coin_simulator():
    while True:
        choices=["heads","tails"]
        guess= input("Head or Tails? ").lower()
        if guess not in choices:
            print("Enter valid input")
        result=random.choice(choices)
        if guess==result:
            print("congratulations!\nYou guessed right")
        else:
            print("You guessed wrong!\nBetter luck next time")
        again=input("Do you want to play again? (y/n) ").lower()
        if again!="y":
            break
print("Welcome to coin toss simulator")
input("press Enter to play" ) 
coin_simulator()       