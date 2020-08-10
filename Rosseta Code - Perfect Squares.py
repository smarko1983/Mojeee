
# Perfect squares from 1 to 100
# Not my code
# 100 doors problem on Rosseta Code
# https://rosettacode.org/wiki/100_doors
for i in range(1, 101):
    if (i**0.5) % 1 != 0:
        state='open'
    else:
        state='close'
    print("Door {}:{}".format(i, state))



