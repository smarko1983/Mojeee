
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








