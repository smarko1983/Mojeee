# Factorial function - very inefficient :)))
n = int(input("Please: "))
square = 1
count = 1
fact = 1
for k in range(1, n + 1):
    fact = k * fact
    print(count, ":", fact)
    count += 1
    print("***********************************")


# Factorial - much better
n = int(input("Please enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)