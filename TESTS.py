# my first try, does not work because if we take that x1 = 3, y1 = 7, x2 = 5, y2 = 6, it would not work
# at all
# x1 = int(input("king's position horizontal: "))
# y1 = int(input("king's position vertical: "))
# x2 = int(input("distination position horizontal: "))
# y2 = int(input("destination position vertical: "))
#
# sum1 = x1 + y1
# sum2 = x2 + y2
#
# if sum2 - sum1 == 1 or sum2 - sum1 == -1:
#     print("Our king can go there")
# else:
#     print("Our king can NOT go there")



# my 2nd try, it worked, version with exclusion principle
# x1 = int(input("king's position horizontal: "))
# y1 = int(input("king's position vertical: "))
# x2 = int(input("distination position horizontal: "))
# y2 = int(input("destination position vertical: "))
#
# if (x1 - x2 > 1 or y1 -y2 > 1)  or (x2 - x1 > 1  or y1 - y2 > 1):
#     print("We can't go there with our king :( ")
# else:
#     print("Our king can go there :) ")




# my 3rd try,  version - inclusion
# x1 = int(input("king's position horizontal: "))
# y1 = int(input("king's position vertical: "))
# x2 = int(input("distination position horizontal: "))
# y2 = int(input("destination position vertical: "))
#
# if  (-1 <= x1 - x2 <=  1)   and  (-1 <= y1 - y2 <= 1):
#     print("Our king can go there :) ")
# else:
#     print("We can't go there with our king :( ")

# n1 = int(input("enter number 1:  "))
# n2 = int(input("enter number 2:  "))
# n3 = int(input("enter number 3:  "))
#
# if n1 > n2 > n3:
#     print("they are in decreasing order")
# elif n1 < n2 < n3:
#     print("they are in increasing order")
# else:
#     print("they are neither in an increasing nor decreasing order")




# 1 2 5 in order
# 1 5 2 not in order
# 5 2 1 in order
# 1 2 2 in order

# n1 = int(input("enter number 1:  "))
# n2 = int(input("enter number 2:  "))
# n3 = int(input("enter number 3:  "))
#
# if n1 == n2 == n3:
#     print("they are equal")
# elif n1 >= n2 >= n3   or n1 <= n2 <= n3:
#     print("in order")
# else:
#     print("not in order")








# **************************************************************************************************************************
# GCD
# divisor = max - 1
# while True:
#     divisor = max - 1
#     if divisor % max == 0 and divisor % min == 0:
#         print("The GCD is: ", divisor)
#         break


# **************************************************************************************************************************




# *******************************************************************************************************************************
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# it works, tested
# total = 0
# for i in range(1, 1000):
#     if i % 3 == 0   or  i % 5 == 0:
#         total += i
#     print(total)



# my modification of the problem above: print all the numbers up to 1000 which are divisible by 3 or 5
# total = 0
# i = 0
# while total < 1000:
#     i += 1
#     if i % 3 == 0 or i % 5 == 0:
#         print("i is: ", i)
#         if total >= 1000:
#             break
#         print("total is: ", total)
#         total += i

# *******************************************************************************************************************************




# *******************************************************************************************************************************
# Project Euler Question 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# it works, tested
# a = 0
# b = 1
# fib = 0
# target = 4_000_000
# sum = 0
#
# while fib < target:
#     fib = a + b
#     a = b
#     b = fib
#     if fib >= target:
#         break
#     if fib % 2 == 0:
#         sum = sum + fib
#     print(sum)

# *******************************************************************************************************************************



# *******************************************************************************************************************************

# Project Euler problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# num = 600851475143
num = 10
product = 1
divisor = 1
store = []

while product != num:  # I plan to multiply prime factors to get the num
    divisor += 1
    print("The divisor is: ", divisor)

    # 1st checking if it is divisible by divisor
    if num % divisor == 0:
        print(num / divisor )

        # now checking if that number is a prime
        for i in range(2, divisor):
            if divisor % i == 0:
                break
            print("the store is: ", store)
            store.append(divisor)

            for j in store:
                product = product * j

print(product[-1])




# product =




















# *******************************************************************************
# These are some of he variations that came to mind which I can use to test
# my students; NOT PROJECT EULER

# with this solution, my CPU will die :)))
# also, this solution works for this number,
# but not for the , let's say, 800....because it is finding the DIVISORS, but
# not PRIME FACTORS
# A question would be something like:
# Find all the divisors of 800
# num = 800
# for i in range(2, num):
#     if num % i == 0:
#         factor = i
#         print(factor)




# This program finds the SMALLEST FACTOR
# num = 900
# for i in range(num - 1 , 2, -1):
#     if num % i == 0:
#         num = num / i
#         largest_factor = i
#         print(largest_factor)









# *******************************************************************************

# one way
# year = int(input("enter a year:  "))
#
# if (year % 100 == 0 and year % 4 == 0)    and (year % 400 != 0):
#     print("not a leap year")
# elif (year % 4 == 0 and year % 100 != 0)  or year % 400 == 0:
#     print("leap year")



# 2nd way- this is a good way if you want to have only one print
# year = int(input("enter a year:  "))
# leap_year = True
# if year % 4 == 0:
#     leap_year = True
#     if year % 400 ==0:
#         leap_year = True
#     else:
#         if year % 100 == 0:
#             leap_year = False
# else:
#     leap_year = False
#
# if leap_year is False:
#     print("not a leap year")
# else:
#     print("leap year")

# *******************************************************************************








