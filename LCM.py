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