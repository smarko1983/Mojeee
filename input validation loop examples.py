# This is what I have been talking about...inpud validation loop examples

# input validation loop 1
name = input("What is your name:  ")
while name != "John":
    print("go on, guess again")
    name = input("Please enter a name again:  ")
    if name == "John":
        print("bye byeee...")
else:
    print("wow, you did it in first try, niiice!")


# Input validation loop 2
age = int(input("please enter your age:  "))
while age < 18:
    print("you are too young")
    age = int(input("How old are you say again: "))

print("You are 18 and older, you can go to see El Classico")