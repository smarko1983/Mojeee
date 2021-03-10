# LCM - LEast Common Multiple

x = int(input("Please enter a number:  "))
y = int(input("Please enter a number:  "))
if x > y:
    x, y = y, x   # swapping the variables
else:
    for i in range(y, x*y + 1, y):
        if (i % y == 0) and (i % x == 0):
            print("lcm of " + str(x) + " and " +  str(y) + " is: ", i)
            break
            
            
# 2nd version functional version- I made it again after some time, and the logic was almost the same
def lcm(num1, num2):
    while True:
        if num1 < 0 or num2 < 0:
            return "LCM stands for positive numbers only, go "
        else:
            if num1 > num2:
                smaller = num2
            elif num2 > num1:
                smaller = num1
            else:
                return "The lcm is " + str(num1)  # it could also be num2 since they are the same
        for increaser in range(smaller, num1*num2 + 1, smaller):  # we are increasing it by lower out of 2 numbers
        # because I forgot to add +1 in the num1*num2 in the for loop, it costed me 15 minutes of debugging
            if increaser % num1 == 0 and increaser % num2 == 0:
                return "LCM is: " +  str(increaser)

print(lcm(4, 9))
print(lcm(4, 12))
print(lcm(4, 8))
print(lcm(4, 5))
print(lcm(15, 4))
print(lcm(2, 2))
print(lcm(9, 9))
