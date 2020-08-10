# Grade 7, Week 2

# 1. Boolean algebra modulo and integer division, comparison operators and string comparison (page 111) review and a short quiz for the students
# 2. Variables and if else statements review
# 3. Presenting elif control structure, as well as nested if else statements
# 4. Assessment

# print(chr(65))
# print(ord(" "))
# for number in range(6):
#     print(number)


# 1. Review of Boolean Algebra

# Quiz for the students:
# Write True,False or a number  next to each of these expressions:
# print((False or True) and True)
# print(True and (True and False))
# print(not(True or False))
# print(not(not(not(False or False))))
# print(not(False and True) and (not(False and True)))
# print(20 % 9)
# print(20 // 6)
# print((2**3 + 7//3) % 4)
# print("This is FLIS CS" == "This is CS FLIS")
# print("Hey" != "hey")
# print(False == False)

# num = int(input("enter a num, now! :  ")
# for x in input("e"):
#     for y in range (1,11): print (int(x) * y)




# 2. Students do 3 questions:

# 1) Ask a friend what is the temperature in Celcius outside. If it is less than zero,
# you need to output (print) that you are stay home. If it's more, you need to output that you are going outside.


# 2) Ask for an input from an user. If the number is divisible by 3 and 5, print "it is", if it is not, print "it is NOT"

# 3) You are working as a security guard at the book fair. A security guard told 3 girls that they could go in only if all of them
# knew their passwords. If only one of them does not know the password, he would deny the entrance to all 3 of them. The secret passwords
# are as follows:
# 1st girl:"Blossom"
# 2nd girl:"Bubbles 22"
# 3rd girl:"Buttercup"
# Ask the girls their passwords, and if they are correct, let them in. If not, tell them to go back.




# 3. Presenting elif control structure, as well as nested if else statements



# Demo 1
# n = 9
# if n > 10:
#     print("go on...")
# else:
#     if n > 65:
#         print("go on 2")
#     else:
#         if n > 8:
#             print("go on 3")
#         else:
#             print("enough")
#             
#     
# # Demo 2   
# if n > 10:
#     print("go on")
# elif n > 65:
#     print("go on 2")
# elif n > 8:
#     print("go on 3")
# else:
#     print("enough")



# demo 3
# n = 9
# if n > 10:
#     print("on")
# elif n > 7:
#     if n > 5:
#         print("over")   
#     else:
#         print("the road ends here")



# demo 4
# n = 9
# if n > 10:
#     print("on")
# elif n > 7:
#     if n > 5:
#         print("over")
#     elif n > 3:
#         print("I am NOT going to be printed")
#     else:
#         print("the road ends here")




# demo 5
# n = 9
# if n > 10:
#     print("on")
# elif n > 7:
#     if n > 5:
#         print("over")
#     elif n > 3:
#         print("I am NOT going to be printed")
#     else:
#         print("the road ends here")
        
# demo 6
# n = 9
# if n > 10:
#     print("on")
# elif n > 7:
#     if n > 5:
#         print("over")
#     if n > 3:
#         print("I AM going to be printed")
#     else:
#         print("the road ends here")





# 4.1 - Pre Warmup - these exercises are not so difficult. The emphasis here is on completion time.


# 1) Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.

# 2) Write a program that reads an integer number and prints its previous and next numbers

# 3) Write a program that asks two people for their names; stores the names in variables called name1 and name2; says hello to both of them. 

# 4) Write a script that asks a user for a number. The script adds 3 to that number. Then multiplies the result by 2, subtracts 4, subtracts twice the original number, adds 3, then prints the result.

# 5) Given any integer number, print its last digit. For example, if someone inputs 453, you need to output 3. If someone enters 230, you need to output 0.
 
# 6) Ask the user to enter a number from 1 to 10. If that number to the power of 4 is equal to  number  16, or that number to the power of 2 is equal to 16, print a message: "I know that you entered either 2 or 4". If not, print "it is definetely not 2 or 4 that you entered!"
 
# 7) Ask the user to enter a number from 1 to 6. If that number is odd and that number is different than 5 and 1, print "I know that the number you entered is 3, ha! ". If not, print "I for sure know that it is not 3"












# • Students do: 
# x = False
# y = “”      # empty string
# You have 3 tasks to do where you will see the difference when comparing:
# 1) compare x and y
# 2) compare the Boolean values of x and y
# 3) compare the types of x and y


# print(chr(65))
# print(ord("A"))



# 4.2 Assesment - repeat the same example as I gave - 3 questions

# 1) Ask the user to enter 2 numbers and see which one of them is smaller and output that

# 2) Ask the user to enter a number. If that number is smaller then 20, multiply it by 3. If it's bigger, than subtract 15 from it

# 3) Ask the user for a number. Check if that number is negative, positive, or zero. Write the program in two ways:
# 1st way: using elif statements
# 2nd way: using nested if else statements

# 4) Ask the user to enter a number between 9 and 9999. Write a program to determine if that number has 2,3 or 4 digits.

# 5) For a football match this season, prices vary depending on the age. You are selling tickets and your job is to ask
# a buyer how old is he, so that you can charge him the ticket based on his age. Even more, you are going to write a program which does that.
# if he is younger than 11, he is not eligible to buy a ticket
# if he is older than 11, you need to print that he is eligible to watch the football match
# if he is less than 20 or older than 60 years old, the ticket price for him is 12$
# if he is between 20 and 60, the ticket price is 20$




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
# elif (int(grade - int(grade))  * 10) == 0 or (int(grade - int(grade)) * 10) == 5 :
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


# what is the error here? Even if we score = int(input("please enter  a num:  ")), the would be an error.
# score = 75
# if score >= 60.0:
#     grade = ' D '
# elif score >= 70.0:
#     grade = ' C '
# elif score >= 80.0:
#     grade = ' B '
# elif score >= 90.0:
#     grade = ' A '
# else:
#     grade = ' F '
# print( grade )


# Demo 1
# n = 9
# if n > 10:
#     print("go on...")
# else:
#     if n > 65 :
#         print("go on 2")
#     else:
#         if n > 8:
#             print("go on 3")
#         else:
#             print("enough")
#
#
# Demo 2
# n = 10
# if n > 15:
#     print("go on")
# elif n > 65:
#     print("go on 2")
# elif n > 6:
#     print("go on 3")
#     if n > 8:
#         print("go on 444")
# else:
#     print("enough")
    


     


# Students do: Classwork review questions: 
# 1)      Explain how short-circuit evaluation works with the and and or operators.
# 2)      When the program compares the strings, what does it actually compare?
# 3)      Write an if statement that displays the message “The number is valid” if the
#         value referenced by speed is within the range 0 through 200.
# 4)      Write an if statement that displays the message “The number is not valid” if the value referenced by speed is outside the range 0 through 200.









 
