import argparse
import string

'''
# TODO
1. Find a solution for the index error =>
    The error was caused due to the -s parameter having an shift value over the range of the list
    E.g if -s is 3 and the letter is z it would case an indexError.
'''

def main():
    
    Lowercase_Letters = string.ascii_lowercase
    Uppercase_Letters = string.ascii_uppercase

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", required=True, type=str, help="Indicate the text you want shift the values")
    parser.add_argument("-s", required=True, type=int, help="Specify the shift value E.g. 3 to shift letter to 3 spaces.")
    args = parser.parse_args()

    cipherText = []
    for i in args.t:
        try:
            if i.isupper():
                index = Uppercase_Letters.index(i)
                newChar = Uppercase_Letters[index + args.s]
                cipherText.append(newChar)
            else:
                index = Lowercase_Letters.index(i)
                newChar = Lowercase_Letters[index + args.s]
                cipherText.append(newChar)
        except:
            if i.isupper():
                currentIndex = Uppercase_Letters.index(i) + 1
                remainingNumberOfLetters = 26 - currentIndex
                newChar = Uppercase_Letters[args.s - remainingNumberOfLetters - 1]
                cipherText.append(newChar)
    
    
    print(''.join(cipherText))

main()