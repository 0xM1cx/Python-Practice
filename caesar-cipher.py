import argparse
import string

'''
# TODO
1. Start commenting on the different functions of each line
2. Add an args and feature for ciphering text inside files
3. Add an args and feature for deciphering text that is both inside files and command line args
4. Add a feature to output cipher text to file
5. Make a readme file for this program
'''

def main():
    
    Lowercase_Letters = string.ascii_lowercase
    Uppercase_Letters = string.ascii_uppercase

    parser = argparse.ArgumentParser(description="This converts your text to a caesar cipher text. You can specify the shift value from 1 - 25")
    parser.add_argument("-t", required=True, type=str, help="Indicate the text you want shift the values")
    parser.add_argument("-s", required=True, type=int, help="Specify the shift value E.g. 3 to shift letter to 3 spaces. You can only have 1 - 25 as shift value")
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
            else: 
                currentIndex = Lowercase_Letters.index(i) + 1
                remainingNumberOfLetters = 26 - currentIndex
                newChar = Lowercase_Letters[args.s - remainingNumberOfLetters - 1]
                cipherText.append(newChar)
    
    print(''.join(cipherText))

main()
