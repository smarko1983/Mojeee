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

number = 48
primes = prime_factorization_func(number)
print("Number", number, "is comprised of the prime numbers: ", primes)
