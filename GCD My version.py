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