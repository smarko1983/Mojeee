# GCD - iterative aproach
num1 = 720
num2 = 160
if num1 > num2:
    maximum = num1
else:
    maximum = num2

divisor = maximum - 1
while True:
    divisor = divisor - 1
    if num1 % divisor == 0 and num2 % divisor == 0:
        print("The GCD is: ", divisor)
        break


# 2nd more thourough version
x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))

if x > y:
    max = x
    min = y
else:
    min = x
    max = y


divisor = max - 1
while True:
    divisor = divisor - 1

    if max % divisor == 0 and min % divisor == 0:
        print("The GCD is: ", divisor)
        break



# GCD with recursive function - found online, looks really cool
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD = gcd(a,b)
print("GCD is: ")
print(GCD)

# explanation of the recursive function:
# 1. User must enter two numbers.
# 2. The two numbers are passed as arguments to a recursive function.
# 3. When the second number becomes 0, the first number is returned.
# 4. Else the function is recursively called with the arguments as the second number and the remainder when the first number is divided by the second number.
# 5. The first number is then returned which is the GCD of the two numbers.
# 6. The GCD is then printed.


# ************************* UPDATE 12.3.2021 *****************************************
# I made more versions of the GCD program. 


# Python program to find the greatest common divisor

# 1st method - by using the LCM. By the formula, GCD(a,b) = (a*b)/LCM(a,b)
# We already calculated the LCM above, but I have rewritten it so that it returns the numbers instead of strings
# def lcm(num1, num2):
#     while True:
#         if num1 < 0 or num2 < 0:
#             return "LCM stands for positive numbers only, go "
#         else:
#             if num1 > num2:
#                 smaller = num2
#             elif num2 > num1:
#                 smaller = num1
#             else:
#                 return num1
#         for increaser in range(smaller, num1*num2 + 1, smaller):
#             if increaser % num1 == 0 and increaser % num2 == 0:
#                 return increaser
#
#
# def gcd(a,b , lcm_for_gcd = lcm(10,25)):  # keyword aproach
#     print(lcm_for_gcd)
#     if a < 0 or b < 0:
#         return "GCD should be calculated for positive integers"
#     else:
#         return int((a * b) / lcm_for_gcd)
#
# print(gcd(10, 25))


# 1st method VARIATION - not calling it from the keyword parameter. It is structured better in this way
# def gcd(a,b ):  # keyword aproach
#     def lcm(num1, num2):
#         while True:
#             if num1 < 0 or num2 < 0:
#                 return "LCM stands for positive numbers only, go "
#             else:
#                 if num1 > num2:
#                     smaller = num2
#                 elif num2 > num1:
#                     smaller = num1
#                 else:
#                     return num1
#             for increaser in range(smaller, num1 * num2 + 1, smaller):
#                 if increaser % num1 == 0 and increaser % num2 == 0:
#                     return increaser
#
#     if a < 0 or b < 0:
#         return "GCD should be calculated for positive integers"
#     else:
#         return int((a * b) / lcm (a,b))
#
# print(gcd(10, 25))
# print(gcd(25,10))
# print(gcd(6,8))
# print(gcd(42,42))
# print(gcd(7,8))
# print(gcd(8,8))
# print(gcd(5,5))


# 2nd method - using the brute force , raw aproach
#
# def gcd ( num1, num2):
#     if num1 > num2:
#         bigger = num1
#     else:
#         bigger = num2
#     for divisor in range(bigger, 0, -1):
#         if num1 % divisor == 0 and num2 % divisor == 0:
#             return f"The GCD of {num1} and {num2} is: ", divisor
#
# print(gcd(10, 25))
# print(gcd(25,10))
# print(gcd(6,8))
# print(gcd(42,42))
# print(gcd(7,8))
# print(gcd(8,8))
# print(gcd(5,5))
# print(gcd(68,48))


# 3rd method  - Using prime factorization - in progress, not finished yet
# Finally finished
def gcd(a,b):
    def prime_factorization_func(num):
        res = []
        divisor = 2
        if num < 2:
            return "That number does not have prime factorization"
        while divisor  < num:
            if num % divisor == 0:
                num = num / divisor
                res.append(divisor)
            else:
                divisor = divisor + 1
        res.append(int(num))
        return  res
    factors_of_a = prime_factorization_func(a)
    print(factors_of_a)
    factors_of_b = prime_factorization_func(b)
    print(factors_of_b)
    new_list=[]
    product = 1
    print("a is now: ",a)
    print("b is now: ",b)
    for element1 in factors_of_a:
        print("Index of element 1 is now: ", factors_of_a.index(element1))
        if element1 in factors_of_b:
            new_list.append(element1)
            factors_of_b.remove(element1)
    for el in new_list:
        product *= el
    return product


result = gcd(100,250)
print()
