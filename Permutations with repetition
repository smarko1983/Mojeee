# the code is far from perfect. I made it so that I could do something for my other project. It is a modified program of this post from stackoverflow:
# https://stackoverflow.com/questions/3099987/generating-permutations-with-repetitions

import itertools


def permutations_with_repetition(iterable):
    '''This function gives us the number of permutations with repetitions. In addition, it also counts them. We can pass x = [1, 2, 3, 4, 5, 6] as argument and see'''


    increaser = 1
    counter = 1
    total = 0  # total number of permutations with repetitions
    for i in range(1,4):
        perms = [p for p in itertools.product(iterable, repeat=increaser)]

        print( counter, "--->", perms, end="\n\n\n")  # shows us how many elements does our list have and prints those elements

        increaser += 1
        counter += 1

        # here we are counting the total number of elements and the element_sum of certain length. For example, length 2 of 6 elements will have 36 permutations.
        element_sum = 0   # the sum of the number of certain length
        for element in perms:
            element_sum = element_sum + 1
        print("the element sum is: ", element_sum)
        total += element_sum
        print("the total sum is: ", total, end="\n\n\n")



permutations_with_repetition([1, 2, 3, 4, 5, 6])
