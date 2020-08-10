import itertools
import string
import random

letters = ["A", "B", "C"]

def password(results):
    for i in results:
        k = str("".join(i))
        print(k)
        if k == "BAB":
             print("I found your password, it is: {} ".format(k))
             break




def all_repeat(letters, rno):
  chars = list(letters)
  results = []
  for c in itertools.product(chars, repeat = rno):
    results.append(c)
  return results


password(all_repeat(letters, 3))



# letters = itertools.permutations(letters, len(letters))
# for i in letters:
#     add = "".join(i)
#     print(add)


# letters = list(string.printable)
# letters = random.choices(letters,k = 3)
# password(letters)










# print(help(combinations_with_replacement))