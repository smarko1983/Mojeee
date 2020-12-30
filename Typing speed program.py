import time

# print(time.gmtime()[5]) # extracting the number of seconds

# print(time.ctime())  # extracts the current time, date, month

# start = time.time()
# print("Starting time: ", start)
# time.sleep(5)
# end = time.time()
# print("Ending time: ",end)
#
# print("Time elapsed: ", end - start)



# This is a program which measures how fast can we type.
# Key statistics:
# 1) Overall duration (how much seconds did we need to type)
# 2) Number of atempts
# 3) Last atempt - in how many seconds did we type
# 4) average typing speed for all atempts
#

import time

# text = "Ovo je test za brzo kucanje. Mi cemo sada izmeriti koliko brzo mozemo da kucamo. Idemo! Lalalalala mi " \
#         "pevamo, la la la laaa. "
# print("This is what you need to type: \n", text)


duration = 0
tries = 0
last_atempt = 0
average = 0
sum_of_all_times = 0

starting_time = time.time()  # the starting time of our whole program
while True:
    text = "Ovo je test za brzo kucanje. Mi cemo sada izmeriti to."

    print("This is what you need to type:\n", text, "\n", "*"*50)
    start_time = time.time()
    my_text = input("Start typing below: \n")
    tries += 1

    if my_text == text:
        end_time = time.time()
        last_atempt = end_time - start_time
        duration = end_time - starting_time
        average = duration / tries
        break
    print("Try again.")



print("The duration is: ", duration)
print("The number of tries is: ", tries)
print("Last atempt (in second): ", last_atempt)
print("The average is: ", average)
