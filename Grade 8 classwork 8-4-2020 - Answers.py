
# Grade 8 classwork 8-4-2020 - Answers:

# 1) Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
# uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

# for i in range(10, 31, 5):
#     burned = 4.2 * i
#     print(burned)
#
# print("-------")
#
# i = 10
# while i >= 10 and i <= 30:    # how can we rewrite this? Question for Matthew, Steve, Ling, Eugene, and Chloe
#                               # also, how can we check if variable i was out of range if it was inputed?
#     burned = 4.2 * i
#     i += 5
#     print(burned)





# 2) 2. Budget Analysis
# Write a program that asks the user to enter the amount that he or she has budgeted for
# a month. A loop should then prompt the user to enter each of his or her expenses for the
# month and keep a running total. When the loop finishes, the program should display the
# amount that the user is over or under budget.

# budget = int(input("How much have you budgeted this month user, please tell me?"))
# answer = "yes"
# total = 0
# while answer == "yes":
#     user = int(input("How much money is this expense? "))
#     total = total + user
#     print(total)
#     answer = input("If you want to continue the calculation, write \"yes\" ")
#
# print("the expenses are: " + str(total))
#
# if budget - total >= 0:
#     print("you are on a positive side, yes")
# else:
#     print("your expenses are bigger than the budget")





# 3)    This question is about chess and legal moves of one of the pieces in a game, called the rook.
#       Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
#       The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.
#       The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.
#       The program needs to ask the user if he/she wants to do it again, as well as to stop the calculation.

# coordinate1 = int(input("Horizontal x axis of your current rook position please, what number?  "))
# coordinate2 = int(input("Vertical y axis of your current rook position please, what number?  "))
# destination1 = int(input("Horizontal x axis of the destination please, what number?  "))
# destination2 = int(input("Vertical y axis of the destination please, what number?  "))
#
# if coordinate1 == destination1 or coordinate2 == destination2:
#     print("The rook can make that move")
# else:
#     print("the rook can not make that move, it is illegal")






# 4)
# Given two cells of a chessboard. If they are painted in one color, print the word YES,
# and if in a different color - NO.
# The program receives the input of four numbers from 1 to 8,
# each specifying the column and row number, first two - for the first cell,
# and then the last two - for the second cell.


# 1st solution
# cell_1_horizontal = int(input("Please enter the horizontal axis:  "))
# cell_1_vertical =   int(input("Please enter the vertical axis:  "))
# dest_2_horizontal = int(input("Please enter the horizontal axis:  "))
# dest_2_vertical =   int(input("Please enter the vertical axis:  "))
# user = int(input("I command you, enter numbers from 1 to 8!"))
#
# while not(0 < user < 9):
#     print("go back and enter numbers from 1 to 8")
#     continue
# if (cell_1_horizontal % 2 == 1 and cell_1_vertical % 2 == 1)  and (dest_2_horizontal % 2 == 1 and dest_2_vertical  % 2 == 1):
#     print("Those two squares  are black")
# elif (cell_1_horizontal % 2 == 0 and cell_1_vertical % 2 == 0) and (dest_2_horizontal % 2 == 0 and dest_2_vertical  % 2 == 0):
#     print("Those two squares are black again")
# elif (cell_1_horizontal % 2 == 1 and cell_1_vertical % 2 == 0)  and (dest_2_horizontal % 2 == 1 and dest_2_vertical  % 2 == 0):
#     print("Those two squares are white")
# else:
#     print("Those two squares  are white")


# 2nd solution
# x1 = int (input("write x coordinate of the first cell: "))
# y1 = int (input ("write the y coordnate of th first cell: "))
# x2 = int (input("write x coordinate of the second cell: "))
# y2 = int (input("write y coordinate of the second cell: "))
#
# if (x1%2 == y1%2 ==  x2%2 == y2%2 == 1) or \
#         (x1%2 == y1%2 == x2%2 == y2%2 == 0) or \
#         (x1%2 == y2%2 == 1 and x2%2 == y1%2 == 0) or \
#         (x1%2 == y2%2 ==0 and y1%2 == x2%2 == 1) or \
#         (x1%2 == x2%2 == 0 and y2%2 == y1%2 == 1) or \
#         (x1%2 == x2%2 == 1 and y1%2 == y2%2 == 0):
#     print ("yes")
# else:
#     print ("no")



# 3rd solution
# x1 = int(input("Please enter the first coordinate of your cell: "))
# y1 = int(input("Please enter the second coordinate of your cell: "))
# x2 = int(input("Please enter the first coordinate of your other cell: "))
# y2 = int(input("Please enter the second coordinate of your other cell: "))
# if (x1 + y1 + x2 + y2) % 2 == 0:
#     print('YES')
# else:
#     print('NO')




















