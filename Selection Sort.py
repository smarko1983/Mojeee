
# This is my way...the code could be improved but it's not bad at all
# later I saw that I could have reused i instead of adding variable count

def selection(lista):
    count = 0
    for i in range(len(lista) - 1):
        minimum_index = i    # starting from 0
        minimum_element = lista[i]   # starting from 0
        for j in range(count + 1, len(lista)):
            if lista[j] < lista[minimum_index]:  # looking for a smaller minimum index
                minimum_index = j  # if we find a smaller minimum index, than it is j
                minimum_element = lista[j]  # if we find a smaller minimum element, than it is lista[j]
        lista[i], lista[minimum_index] = lista[minimum_index], lista[i]
        count += 1
    return lista

listica = [8, -5, 9, 24, 7, 2, -2, -9, 14, 35, -500, 72, -580]
print(selection(listica))


# listurina = [3,9,4,5]
# listurina[0], listurina[3] = listurina[3], listurina[0]
# print(listurina)
# Another way that I saw in one book. This is a cool aproach with 2 functions.


# Finds the smallest value in an array
# def findSmallest(arr):
#   # Stores the smallest value
#   smallest = arr[0]
#   # Stores the index of the smallest value
#   smallest_index = 0
#   for i in range(1, len(arr)):
#     if arr[i] < smallest:
#       smallest_index = i
#       smallest = arr[i]
#   return smallest_index

# # Sort array
# def selectionSort(arr):
#   newArr = []
#   for i in range(len(arr)):
#       # Finds the smallest element in the array and adds it to the new array
#       smallest = findSmallest(arr)
#       newArr.append(arr.pop(smallest))
#   return newArr
#
# print(selectionSort([5, 3, 6, 2, 10]))






