# Please remember this, don't put accumulator variable inside of a loop
# Let's say that we want to add first 10 numbers together...

# this is good
accumulator = 0
for num in range(1,11):
    accumulator = accumulator + num
    print(accumulator)

# this is bad...because the accumulator variable is always reseted to 0, no matter what we add to it
for num in range(1,11):
    accumulator = 0
    accumulator = accumulator + num
    print(accumulator)