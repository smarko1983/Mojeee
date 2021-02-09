l = [1,28,28,34,34,34,34,87,87,87,87,87,87, 97]

# My 1st solution
# l = set(l)
# print(l)

# My 2nd solution - I think that the functional solution is the best. Still, I tried to figure it out how would I do it with loops. My 2nd solution sucks, but I am hoping to improve it.
# The part that took the most to figure out is how to stop the index out of error exception.
list_fill = [l[0]]
list_length = len(l)
index = 0
for element in l:
    if element not in list_fill:
        list_fill.append(element)
    if element != l[-1]:  # this is the line I wrote to offset the "index out of range" exception
        if(l[index] != l[index + 1]) and (element not in list_fill) :
            list_fill.append(element)
        print(list_fill)
        index += 1

print(list_fill)


# my 3rd solution - I was looking at the list and I figured out a much simpler solution. I am now wondering what was
# I thinking when I wrote the code for the second solution
list_fill = []
for element in l:
    if element not in list_fill:
        list_fill.append(element)

print(list_fill)
