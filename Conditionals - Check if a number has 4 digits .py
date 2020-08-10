num = int(input("please enter a number between 9 to 9999"))
num1 = num //10
num2 = num //100
num3 = num //1000
num4 = num //10000
if num < 9 or num > 9999:
    print("please try again")
elif num1 == 0:
    print("it is one digit")
elif num2 == 0:
    print("it is two digit")
elif num3 == 0:
    print("it is three digit")
else:
    print("it is four digit")



