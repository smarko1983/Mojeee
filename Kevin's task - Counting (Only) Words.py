# Kevin (the GAC student) asked me to help him to write a script that counts the number of the words in a string and their length. The program should return a list and the length of the words
# For example, if the string is "Hi! W*ho are>>> they watching???", the output should be [2, 3, 3, 4, 8]. We must count the punctuation signs.


# 1st version, with string.replace method
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



# 2nd version - without string.replace method - it's more challenging
import string

p = string.punctuation
print(p)

test_string = "!!Tutorials point is. a learning platform"
#original string
print ("The original string is : " + test_string)
# using split() function

test_string.split()
res = test_string.split()
print("The res is: ", res)
# res is equal to  ['!!Tutorials', 'point', 'is.', 'a', 'learning', 'platform']


filtering = [] # words without punctuation marks
new_word = ""


for word in res:  # looping through the list of all the words
    for symbol in p: # picking up each symbol from the punctuation string
        if symbol not in word:  # for example, if ! is not in a word
            for letter in word:
                if letter not in p:
                    new_word = new_word + letter
            filtering.append(new_word)
            print("The new list is: ", filtering) # checking if everything is correct
            new_word = "" # reseting the new word variable. If I did not do that, the new list would containt all the previous words.
            break # we have to break when that cleaning process is finished.

print("filtered list: ", filtering)


# the length of the words in a list
length_of_words_list = []
for word in filtering:
    length_of_words_list.append(len(word))

print("\n\nThe length of words list and this the solution:\n", length_of_words_list)
