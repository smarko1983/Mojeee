
import random

def rock_paper_scissors_game():

    def choose():
        print("Welcome to the rock paper scissors game!")
        start = input("If you want to start, write yes: ")
        if start != "yes":
            print("bye byeee")
            return None
        letters = ["r", "p", "s"]
        me = input("Please enter a letter:  ")
        computer =  random.choice(letters)
        print("the computer choose: ", computer)
        return play(me, computer)


    def play(me, computer):
        if (me == "r" and computer == "s") or (me == "s" and computer == "p") or (me == "p" and computer == "r"):
            return winner()
        elif (me == "r" and computer == "r") or (me == "s" and computer == "s") or (me == "p" and computer == "p"):
            return draw()
        else:
            return looser()


    def winner():
        print(r'''
     |       |
    (| SFAfS |)
     |  #X   |
      \     /
       `---'
       _|_|_''')


    def looser():
        print(r'''
    .     .-""""""-.
       .'  \\  //  '.
      /   O      O   \
     :                :
     |                |  angry...hate loosing!
     :       __       :
      \  .-"`  `"-.  /
       '.          .'
         '-......-'
    ''')


    def draw():
            print(r'''
    .----------------.  .----------------.  .----------------.  .----------------.
    | .--------------. || .--------------. || .--------------. || .--------------. |
    | |  ________    | || |  _______     | || |      __      | || | _____  _____ | |
    | | |_   ___ `.  | || | |_   __ \    | || |     /  \     | || ||_   _||_   _|| |
    | |   | |   `. \ | || |   | |__) |   | || |    / /\ \    | || |  | | /\ | |  | |
    | |   | |    | | | || |   |  __ /    | || |   / ____ \   | || |  | |/  \| |  | |
    | |  _| |___.' / | || |  _| |  \ \_  | || | _/ /    \ \_ | || |  |   /\   |  | |
    | | |________.'  | || | |____| |___| | || ||____|  |____|| || |  |__/  \__|  | |
    | |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------'
            ''')

    # starting a game  - calling a choose function
    choose()

rock_paper_scissors_game()





# an alternative aproach - nesting the play function

# def rock_paper_scissors_game():
#
#     def choose():
#
#         print("Welcome to the rock paper scissors game!")
#         start = input("If you want to start, write yes: ")
#         if start != "yes":
#             print("bye byeee")
#             return None
#         letters = ["r", "p", "s"]
#         me = input("Please enter a letter:  ")
#         computer =  random.choice(letters)
#         print("the computer choose: ", computer)
#         # I modified this part, there is no return here
#
#
#         def play():
              # if there was a return in the choose function, we could possible do me, computer = choose()
#             if (me == "r" and computer == "s") or (me == "s" and computer == "p") or (me == "p" and computer == "r"):
#                 return winner()
#             elif (me == "r" and computer == "r") or (me == "s" and computer == "s") or (me == "p" and computer == "p"):
#                 return draw()
#             else:
#                 return looser()
#         play()    # I modified this part because I nested the play function and later called it. This means that
#         the variables me and computer are available in the play function
#
#
#     def winner():
#         print(r'''
#      |       |
#     (| SFAfS |)
#      |  #X   |
#       \     /
#        `---'
#        _|_|_''')
#
#
#     def looser():
#         print(r'''
#     .     .-""""""-.
#        .'  \\  //  '.
#       /   O      O   \
#      :                :
#      |                |  angry...hate loosing!
#      :       __       :
#       \  .-"`  `"-.  /
#        '.          .'
#          '-......-'
#     ''')
#
#
#     def draw():
#             print(r'''
#     .----------------.  .----------------.  .----------------.  .----------------.
#     | .--------------. || .--------------. || .--------------. || .--------------. |
#     | |  ________    | || |  _______     | || |      __      | || | _____  _____ | |
#     | | |_   ___ `.  | || | |_   __ \    | || |     /  \     | || ||_   _||_   _|| |
#     | |   | |   `. \ | || |   | |__) |   | || |    / /\ \    | || |  | | /\ | |  | |
#     | |   | |    | | | || |   |  __ /    | || |   / ____ \   | || |  | |/  \| |  | |
#     | |  _| |___.' / | || |  _| |  \ \_  | || | _/ /    \ \_ | || |  |   /\   |  | |
#     | | |________.'  | || | |____| |___| | || ||____|  |____|| || |  |__/  \__|  | |
#     | |              | || |              | || |              | || |              | |
#     | '--------------' || '--------------' || '--------------' || '--------------' |
#      '----------------'  '----------------'  '----------------'  '----------------'
#             ''')
#
#     # starting a game  - calling a choose function
#     choose()
#
# rock_paper_scissors_game()






# 3rd version - I added the total number of wins, loses, draws, and games

import random


def rock_paper_scissors_game():

    wins = 0
    loses = 0
    draws = 0
    games = 0

    while True:
        def choose():
            print("Welcome to the rock paper scissors game!")
            letters = ["r", "p", "s"]
            me = input("Please enter a letter:  ")
            computer = random.choice(letters)
            print("the computer choose: ", computer)
            return play(me, computer)

        def play(me, computer):
            nonlocal games, loses, draws, wins
            if (me == "r" and computer == "s") or (me == "s" and computer == "p") or (me == "p" and computer == "r"):
                games = games + 1
                wins = wins + 1
                return winner()
            elif (me == "r" and computer == "r") or (me == "s" and computer == "s") or (me == "p" and computer == "p"):
                games = games + 1
                draws = draws + 1
                return draw()
            else:
                games = games + 1
                loses = loses + 1
                return looser()

        def winner():
            print(r'''
         |       |
        (| SFAfS |)
         |  #X   |
          \     /
           `---'
           _|_|_''')

        def looser():
            print(r'''
        .     .-""""""-.
           .'  \\  //  '.
          /   O      O   \
         :                :
         |                |  angry...hate loosing!
         :       __       :
          \  .-"`  `"-.  /
           '.          .'
             '-......-'
        ''')

        def draw():
            print(r'''
        .----------------.  .----------------.  .----------------.  .----------------.
        | .--------------. || .--------------. || .--------------. || .--------------. |
        | |  ________    | || |  _______     | || |      __      | || | _____  _____ | |
        | | |_   ___ `.  | || | |_   __ \    | || |     /  \     | || ||_   _||_   _|| |
        | |   | |   `. \ | || |   | |__) |   | || |    / /\ \    | || |  | | /\ | |  | |
        | |   | |    | | | || |   |  __ /    | || |   / ____ \   | || |  | |/  \| |  | |
        | |  _| |___.' / | || |  _| |  \ \_  | || | _/ /    \ \_ | || |  |   /\   |  | |
        | | |________.'  | || | |____| |___| | || ||____|  |____|| || |  |__/  \__|  | |
        | |              | || |              | || |              | || |              | |
        | '--------------' || '--------------' || '--------------' || '--------------' |
         '----------------'  '----------------'  '----------------'  '----------------'
                ''')

        # starting a game  - calling a choose function

        choose()
        start = input("If you want to continue, write yes. ").lower()
        if start != "yes":
            print("bye byeee")
            break
    print("Total games: ", games)
    print("Wins: ",wins)
    print("Loses: ", loses)
    print("Draws: ", draws)




rock_paper_scissors_game( )








