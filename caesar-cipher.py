import argparse
from ast import arg
import string

def main():
    
    Lowercase_Letters = string.ascii_lowercase
    Uppercase_Letters = string.ascii_uppercase

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", required=True, type=str, help="Indicate the text you want shift the values")
    parser.add_argument("-s", required=True, type=int, help="Specify the shift value E.g. 3 to shift letter to 3 spaces.")
    args = parser.parse_args()

    cipherText = []
    for i in args.t:
        if i.isUpper():
            index = Uppercase_Letters.index(i)
            newChar = Uppercase_Letters[index + args.s]
            cipherText.append(newChar)
        else:
            index = Lowercase_Letters.index(i)
            newChar = Lowercase_Letters[index + arg.s]
            cipherText.append(newChar)

    print(''.join(cipherText))

main()