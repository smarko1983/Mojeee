# 6) Grades are values between zero and 10 (both zero and 10 included), and
# are always rounded to the nearest half point. To translate grades to the American style, 8.5
# to 10 become an “A,” 7.5 and 8 become a “B,” 6.5 and 7 become a “C,” 5.5 and 6 become
# a “D,” and other grades become an “F.” Implement this translation, whereby you ask the
# user for a grade, and then give the American translation. If the user enters a grade lower
# than zero or higher than 10, just give an error message. You do not need to handle the user
# entering grades that do not end in .0 or .5, though you may do that if you like – in that case,
# if the user enters such an illegal grade, give an appropriate error message.

# grade = float(input("Please enter your grade user: "))
# if  grade < 0 or 10 < grade:
#     print("We said not to do that!")
# elif ((int((grade - int(grade))  * 10)) == 0) or ((int((grade - int(grade))) * 10) == 5 ):
#     if 8.5 <= grade <= 10:
#         print("A")
#     elif 8 >= grade >= 7.5:
#         print("B")
#     elif 7 >= grade >= 6.5:
#         print("C")
#     elif 5.5 <= grade <= 6:
#         print("D")
#     else:
#         print("F")
#
# else:
#     print("we said only .5 and .0")



# 2nd try - 27 minutes
# one mistake that I made: I tested 5.47 % 10 expecting that I would get 0.47 :) then it occured to me that if I
# modulo divided it by 1, that is  5.47 % 1, I would get my decimal part, that is 0.47
# grade = float(input("Please enter your grade user: "))
# decimal_check = grade % 1
# if grade > 10 or grade < 0:
#     print("That's not the way")
# elif decimal_check == 0 or decimal_check == 0.5:
#     if 8.5 <= grade <= 10:
#         print("A")
#     elif 8 >= grade >= 7.5:
#         print("B")
#     elif 7 >= grade >= 6.5:
#         print("C")
#     elif 5.5 <= grade <= 6:
#         print("D")
#     else:
#         print("F")
# else:
#     print("we said only .5 and .0")
#
# # textbook solution:
# from pcinput import getFloat
# grade = getFloat( "Please enter a grade: " )
# check = int( grade * 10 )
# if grade < 0 or grade > 10:
#     print( "Grades have to be in the range 0 to 10." )
# elif check%5 != 0 or check != grade *10:
#     print( "Grades should be rounded to the nearest half point.")
# elif grade >= 8.5:
#     print( "Grade A" )
# elif grade >= 7.5:
#     print( "Grade B" )
# elif grade >= 6.5:
#     print( "Grade C" )
# elif grade >= 5.5:
#     print( "Grade D" )
# else:
#     print( "Grade F" )