import random

#define functions
def coin_flip():
    heads_tails_list = ["Heads", "Tails"]
    response = input("Would you like to flip a coin?")
    if (response.casefold()[0] == "y"):
        while True:
            res = input("Which side of the coin do you pick? (Heads/Tails)")
            lower_res = res.lower()
            heads_or_tails = random.choice(heads_tails_list)
            heads_or_tails_lower = heads_or_tails.lower()
            if (lower_res == "heads") or (lower_res == "tails"):
                if (lower_res == heads_or_tails_lower):
                    print("You won! The coin landed on " + heads_or_tails + "!")
                    break
                elif (lower_res != heads_or_tails_lower):
                    print("Sorry, you lose. The coin landed on " + heads_or_tails + "! Better luck next time!")
                    break
            else:
                print("I am sorry, I do not understand your response. Please answer with heads or tails.")
                continue
    elif (response.casefold()[0] == "n"):
        print("ok")
    else:
        print("I am sorry, I do not understand your response. Please enter a yes or a no.")

#Program Starts
while True:
    coin_flip()


