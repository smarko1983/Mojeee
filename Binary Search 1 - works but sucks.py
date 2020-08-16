# My implementation of the Binary Search Algorithm
# It sucks sooooo much but it works :)))
# it is beggining to be improved

lista = [9, 31, 5, 34,  5, 5, 5, 15, 14, 3, 47, 95, 88, -7, 98, 184, 235, -500, 4]
lista = sorted(lista)
original_lista = lista
print(lista)

element = 3 # the element that we are searching for; we could use the random function there
middle_index = (len(lista) - 1) // 2
guess = lista[middle_index]

while guess in lista:
    if guess > element:
        lista = lista[:  lista.index(guess)]
        print("if the guess is bigger than the element, the lista is: ", lista)
    elif guess < element:
        lista = lista[lista.index(guess) + 1:]
        print("if the guess is smaller than the element, the lista is: ", lista)
    else:
        print("you found your number, it is", element, " and it lies in the index (position) number ",
              original_lista.index(element))
        break

    middle_index = (len(lista) - 1) // 2
    if middle_index < 0:
        print("the element is not in the list")
        break
    print("the middle index is: ", middle_index)
    guess = lista[middle_index]




