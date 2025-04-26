import random
def magic_8_ball():
    responses=["It is Certain.",
               "Without a doubt.",
               "You rely on it.",
               "Yes definitely.",
               "As i see it, Yes.",
               "Signs point to Yes.",
               "Reply hazy, try again.",
               "Ask again later.",
               "Better not tell you now.",
               "Cannot predict now.",
               "Concentrate and ask again.",
               "Don't count on it.",
               "My reply is no.",
               "My sources says no.",
               "Outlook not so good.",
               "Very doubtful."]
    print("Welcome to magic 8 Ball")
    input("Press Enter to play ")
    while True:
        question=input("Ask the Magic 8 Ball a yes/no question.")
        if question.strip()=="":
            print("Please ask areal question.")
        print("Thinking...")
        answer=random.choice(responses)
        print(f"Magi 8 Ball says:{answer}")
        again=input("Do you want ask another question (y/n).").lower()
        if again!="y":
            print("Good bye!")
            break
if __name__=="__main__":
    magic_8_ball()