# Provide a script printing every possible pairs of two letters, 
# only lower case, one by line, ordered alphabetically. 

import string

# Print Every Possible letter pairs
def printLetterPairs():
    letters = string.ascii_lowercase

    for i in letters:
        for b in letters:
            print(i + b) 

def printDistinctPairs():
    lowerCase_letter = string.ascii_lowercase
    for i in lowerCase_letter:
        for b in lowerCase_letter:
            if i != b:
                print(i + b)