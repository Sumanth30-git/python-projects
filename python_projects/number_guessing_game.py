import random
def number_guessing_game():
    print("i'm thinking of a number between 1 and 100")
    number=random.randint(1,100)
    attempts=0
    while True :
        try:
            guess=int(input("Take a guess: "))
            attempts+=1
            if guess>number:
                    print("your guess was too high! try again")
        
            elif guess<number:
                    print("your guess was too low! try again")
            else:
                print(f"congratulayions! you guessed the number in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")
print("welcome to the number guessing game")
input("press Enter to play")
number_guessing_game()
                