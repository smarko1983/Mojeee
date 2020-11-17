import random
import string

# 1st version - as per algorithm what the solution required
# Their algorithm is ok, but it does not fully randomize because everything is in order. For example, uppercase letter will always appear in the first 2 place, and digits will always appear in the last 2 places. That's why I made the second version which is "truly" random

#Main program starts here
# uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
# uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
# lowercaseLetter1 = chr(random.randint(97,122))
# lowercaseLetter2 = chr(random.randint(97,122))
# symbols1 = chr(random.randint(33,47))   # we only took some of the basic symbols, like !, ?, #, +...
# symbols2 = chr(random.randint(33,47))   # we only took some of the basic symbols, like !, ?, #, +...
# digits1 = chr(random.randint(48,57))    # digits from 1 to 9
# digits2 = chr(random.randint(48,57))    # digits from 1 to 9
# password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter1 + symbols1 + symbols2 + digits1 + digits2  # this will not work
# random.shuffle(list(password))
# print(password)



# my 2nd version of the program which is "truly" random
#
# uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
# uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
# lowercaseLetter1 = chr(random.randint(97,122))
# lowercaseLetter2 = chr(random.randint(97,122))
# symbols1 = chr(random.randint(33,47))   # we only took some of the basic symbols, like !, ?, #, +...
# symbols2 = chr(random.randint(33,47))   # we only took some of the basic symbols, like !, ?, #, +...
# digits1 = chr(random.randint(48,57))    # digits from 1 to 9
# digits2 = chr(random.randint(48,57))    # digits from 1 to 9
# password = [uppercaseLetter1, uppercaseLetter2 , lowercaseLetter1 , lowercaseLetter2, digits1, digits2, symbols1, symbols2]
# random.shuffle(password)   # this shuffles it in place, no need to introduce a variable
#
# # converting our list elements to a string
# final_password = ""
# for element in password:
#     final_password = final_password + element
# print(final_password)


# 3rd version

# a = string.ascii_uppercase
# a = list(a)
# a = random.choice(a)
# print(a)

# lista = [random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.choice(string.ascii_lowercase), random.choice(string.punctuation), random.choice(string.punctuation), random.choice(string.digits), random.choice(string.digits)]

# # converting our list elements to a string
# final_password = ""
# for element in lista:
#     final_password = final_password + element
# print(final_password)


# a one liner to convert a list to a string
# print("".join(lista))


# 4th version - a masterpiece :))))
print("".join( [random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.choice(string.ascii_lowercase), random.choice(string.punctuation), random.choice(string.punctuation), random.choice(string.digits), random.choice(string.digits)] ) )
