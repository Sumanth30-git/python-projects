import random
def hangman():
    print("Welcome to hangman")
    input("Press Enter To Play")
    words=["pythona","apple","guitar","flawer","chocolate","adventure"]
    tries=6
    word=random.choice(words)
    print("_"*len(word))
    guessed_letters=[]
    while tries!=0:
        
        guess=input("guess a Letter: ").lower()
        
        if len(guess) != 1:
                print("please enter a single Letter...")
                continue
        if not guess.isalpha():
                print("Please Enter Alpabet")  
                continue
                
        if guess in guessed_letters:
            print("You already guess the letter.")
            continue
        guessed_letters.append(guess)
       
        if guess in word:
            print("good guess!")
        else:
            tries-=1
            print(f"!wrong guess. tries left:{tries}")
        
        s=[value if value in guessed_letters else"_" for value in word]
        print("".join(s))
            
        if "_" not in s:
            print("congratulations! you guess the world.")
            break
        if tries==0:
            print(f"Better Luck Next Time!\nYou Lost all tries\nThe Word is:{word}")
if __name__=="__main__":
    hangman()    
        
        