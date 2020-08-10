# I used Flags just to demonstrate a different style of coding
import random

num= random.randint(0,100)
flag = False
for x in range(1, 7):
    user= int(input("number: "))
    if user==num:
        print(num , "!, you guessed it!")
        flag = True
    elif user > num:
        print("your answer is bigger than the secret number")
    elif num > user:
        print("your number is less than the secret number")
    print("you have", 6 - x, "tries left")
    if 6-x==0:
        print("game over")
        break
    if flag:
        break