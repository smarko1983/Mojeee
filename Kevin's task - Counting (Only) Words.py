# Kevin (the GAC student) asked me to help him to write a script that counts the number of the words in a string and their length. The program should return a list and the length of the words
# For example, if the string is "Hi! W*ho are>>> they watching???", the output should be [2, 3, 3, 4, 8]. We must count the punctuation signs.

import string

p = string.punctuation
# This is a  string of punctuation symbols:   !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

test_string = "H*e*l*l*o Kevin!!! The string without the ?!#/punctuation signs."
#original string

all_words = test_string.split()
print("The res is: ", all_words)
# res is equal to  ['Tutorials', 'point', 'is.', 'a', 'learning', 'platform']

filtering = [] # words without punctuation marks

for word in all_words:  # looping through the list of all the words
    print("Original word: ", word, end=" ")
    for symbol in p: # picking up each symbol from the punctuation string
        if symbol in word:  # for example, if / is  in a word
            word = word.replace(symbol, "")  # the replace method replaces all the occurences of that letter in a
            # word with an empty string "", that is, it removes that letter.

    print("---> Filtered word ", word )
    filtering.append(word)
print("\nfiltered list of words without punctuation: ", filtering,"\n")

total = 0
word_length_list = []
for word in filtering:    # now we just need to measure the words from the filtered list
    print("The word", word, "has", len(word), "characters. ")
    word_length_list.append(len(word))
    total += len(word)

print("The list of the length of all the words: ", word_length_list)
print("***** The total number of characters of all the words: ", total, "*****")
