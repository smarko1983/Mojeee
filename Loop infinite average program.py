# Welcome to our infinite average program. To stop it, you will need to type yes when
# asked if you want to stop the program
count = 0
sum = 0
while count < 5:
    num = int(input("Please, I beg you,  enter a num:  "))
    sum += num
    count += 1
    average = sum / count
    print("And the AVEEERAAGEE IIIIS: ", average)
    if input("Do you want to quit (are you a looser?!):  ") == "yes":
        print("bye byeee")
        break