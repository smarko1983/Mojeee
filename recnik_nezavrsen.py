# Recnik, moj pocetak....
recnik_Marko = {
    "proba": "Ovo je samo isprobavanje",
    "IDE": "Integrated Programming Enviroment - basically, a program win which you can write other programs.",
    "operator": "A thing which combines two operands",
    "Assert": "A sanity check for programers",
    "Program": "A set of instructions for the computer to execute"
}


# testing loop
# for i,j in zip(recnik_Marko, recnik_Marko.values()):
#     print(i,"->", j)


def dictionary_search() -> None:
    '''This function let's the user search for a word in a dictionary. The case where the word is not found is covered'''
    user_search = input("Enter the word that you would like to search: ")
    if user_search in recnik_Marko:
        print("The word is found in our dictionary. Please look at the definition bellow:")
        print(user_search, "--->", recnik_Marko[user_search])
    else:
        print("I am so so so so so soooorryyy, but we do not have that word.")


def dictionary_update():
    '''With this option, we are adding the word to a dictionary'''
    recnik_update_word = input("Please choose a word that you would like to add to the dictionary:  ")
    while recnik_update_word != "no":
        if recnik_update_word not in recnik_Marko:
            recnik_update_definition = input("Please write your definition for the word " + recnik_update_word + " :  ")
            recnik_Marko.update( {recnik_update_word: recnik_update_definition} )
            print("\n", "*" * 100, "\n", "Thank you, the dictionary is now updated. It looks like this: ", recnik_Marko, "\n", "*" * 100, "\n")
        else:
            recnik_update_word = input(
                "That word is already in the dictionary. Please choose another word or type quit to quit the program: ")
            if recnik_update_word == "quit":
                print("You chose to quit the program, byeeee")
                break
            continue

        # asking the user to add one more word
        recnik_update_word = input("If you would like to add another word, please enter yes: ").lower()
        if recnik_update_word != "yes":
            print("The dictionary is closing now...")
            return
        else:
            recnik_update_word = input("Please choose a word that you would like to add to the dictionary:  ")

# dictionary_search()
dictionary_update()

students = {}
