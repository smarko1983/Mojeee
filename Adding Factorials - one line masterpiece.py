# The problem is from the snakify website:  https://snakify.org/en/lessons/for_loop_range/problems/sum_of_factorials/

# normal solution
n = int(input("Please enter a num: "))
fact = 1
sum = 0
for i in range(1, n + 1):
    fact = fact * i
    sum = sum + fact
print(sum)


# One liner, did it in class:
#[ result :=  (k := int(input("Enter the number:"))), (sum1 := 1), print([sum1 := sum1 * num +1 for num in range(k, 1, -1) ] [-1])     ]
