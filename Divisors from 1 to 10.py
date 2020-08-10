# Find the divisors from 1 to 100 - for every number from 2 to 10
divisor = 1
for i in range(1,11):
    divisor += 1
    for k in range(2,101):
        if k % divisor == 0:
            print(k, " can be divided by ", divisor )
        else:
            print("it can't be :(")

    print("**********************")