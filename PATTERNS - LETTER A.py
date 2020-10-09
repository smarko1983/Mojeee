# Question:
# print the capital letter A using nested for loops
#    * * *
#  *       *
#  *       *
#  * * * * *
#  *       *
#  *       *
#  *       *

# 1st atempt - looks cool :)
#  ***
#  ***
#  ***
# *****
# *   *
# *   *
#  ***
#  ***
#  ***
# *****
# *   *
# *   *
# *   *

# rows = 7
# cols = 5
# for row in range(1,8):
#     for col in range(1,6):
#         if (col == 1 or col == 5) and (row != 1 and row != 4) :
#             print("*" + " " * 3 + "*")
#             break
#         elif (col == 4):
#             print("*"*5)
#             break
#         else:
#             print(" " + "*" * 3 + " ")



# 2nd atempt - succesful, with a bit of trial and error
# I feel that the solution could be more simpler though
# rows = 7
# cols = 5
# for row in range(1,8):
#     for col in range(1,2):
#         if (col == 1) and (row == 1) :
#             print(" " + " *" * 3 + " ")
#         elif (row == 4):
#             print("* " * 5)
#             break
#         else:
#             print("* " + " " * 6 + "* ")



# The proposed solution - more elegant with more demanding condition
for row in range(7):
    for col in range(5):
        if ((col == 0 or col == 4)  and (row != 0 )) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
            print("*", end = "")
        else:
            print(end = " ")
    print()
    
