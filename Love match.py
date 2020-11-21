# This is a question from 100 days of code that I solved. The solution can be imrpoved a lot.
# https://repl.it/@appbrewery/day-3-5-exercise#README.md


name1 = "Marko Savic"
name2 = "Danijela Kovacevic"
name_merged = name1 + name2



t = name_merged.count("t")
print(t)
r = name_merged.count("r")
print(r)
u = name_merged.count("u")
print(u)
e = name_merged.count("e")
print(e)

l = name_merged.count("l")
print(l)
o = name_merged.count("o")
print(o)
v = name_merged.count("v")
print(v)
e2 = name_merged.count("e")
print(e)

true = t + r + u + e
print(true)
love = l + o + v + e2
print(love)
true_love = str(true) + str(love)
print("*" * 180)

if int(str(true) + str(love)) < 10 or int(str(true) + str(love)) > 90:
    print("Your score is {}, you go together like coke and mentos.".format(true_love))
elif int(str(true) + str(love)) > 40 and int(str(true) + str(love)) < 50:
    print("Your score is {}, yo go fine together.".format(true_love))
else:
    print("your score is {}".format(true_love))



