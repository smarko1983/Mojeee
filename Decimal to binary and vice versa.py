
# first version decimal to binary
num = int(input("Enter the decimal human: "))
dec = num
remainders = []
if num == 0:
    print("decimal: ",dec, " -----> binary: ", 0)
else:
    while num  != 0:
        remainder = num % 2
        num = num // 2
        remainders.append(remainder)

    rem = reversed(remainders)
    binary = ""
    for i in rem:
        binary =  binary + str(i)
    print("decimal:",dec, " -----> binary:", binary)



# second version decimal to binary - without a list
num = int(input("Enter the decimal human: "))
dec = num
result = ""
if num == 0:
    print("decimal: ",dec, " -----> binary: ", 0)
else:
    while num  != 0:
        remainder = num % 2
        num = num // 2
        result =  str(remainder) + result

    print("decimal:",dec, " -----> binary:", result)



# Binary to decimal
# 110 is 1*2**3 + 1*2**2 + 0*2**0
num = int(input("Please enter the binary number: "))
decimal = 1
result = 0
length = len(str(num)) - 1
# for digit in range(1, len(str(num)) + 1):     potential
for digit in str(num):
    power = 2 ** length
    decimal = int(digit) * power
    result += decimal
    length -= 1

print(result)


# decimal to binary - function version
def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')


# decimal number
number = int(input("Enter any decimal number: "))

decimalToBinary(number)






