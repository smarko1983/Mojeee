# In this version, I used functions to "imitate" a loop

import random

def rock_paper_scissors():

    offered = ["r", "p", "s"]   # r ---> rock,  p ---> scissors, s --->
    def choices():
        c = random.choice(random.choice(offered))  # c is computer
        print("The computer choice is: ", c)
        h = input("Please enter r for rock, p for paper, and s for scissors:  ")  # h is human

        def game():
            # first case ---> the case when a computer wins
            if (c == "r" and h == "s") or (c == "p" and h == "r") or (c == "s" and h == "p"):
                winner = "Computer"
            # second case ---> the case where the human won
            elif (c == "r" and h == "p") or (c == "p" and h == "s") or (c == "s" and h == "r"):
                winner = "Human"
            else:
                print("It is a tie! The game will restart until there is a winner...")
                # winner = game()  # a mistake, it will always remember the state of outside variables
                winner = choices()

            return winner
        return game()

    return choices()


outcome = rock_paper_scissors()
if outcome == "Human":
    print("Power to the people ")
else:
    print("The machines are taking over")
