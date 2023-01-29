import argparse
import string
'''
!! TODO !!
1. Start commenting on the different functions of each line
2. Add an args and feature for ciphering text inside files
3. Add an args and feature for deciphering text that is both inside files and command line args
4. Add a feature to output cipher text to file
'''
def main():
    
    Lowercase_Letters = string.ascii_lowercase # string of lowercase letters
    Uppercase_Letters = string.ascii_uppercase # string of uppercase letters


    parser = argparse.ArgumentParser(description="This converts your text to a caesar cipher text. You can specify the shift value from 1 - 25")
    parser.add_argument("-f", required=False, type=str, help="Indicate the path to the text file")
    parser.add_argument("-t", required=False, type=str, help="Indicate the text you want shift the values")
    parser.add_argument("-s", required=True, type=int, help="Specify the shift value E.g. 3 to shift letter to 3 spaces. You can only have 1 - 25 as shift value")
    args = parser.parse_args()

    cipherText = [] # This stores the ciphered text
    
    # This parses the arguments and performs the shifting of the values
    if(args.t != None):
        for i in args.t:
            try:
                if i.isupper(): # check if its an uppercase letter
                    index = Uppercase_Letters.index(i) # 
                    newChar = Uppercase_Letters[index + args.s]
                    cipherText.append(newChar)
                else:
                    index = Lowercase_Letters.index(i)
                    newChar = Lowercase_Letters[index + args.s]
                    cipherText.append(newChar)
            except:
                if i.isupper(): # Check if its in lowercase
                    currentIndex = Uppercase_Letters.index(i) + 1
                    remainingNumberOfLetters = 26 - currentIndex
                    newChar = Uppercase_Letters[args.s - remainingNumberOfLetters - 1]
                    cipherText.append(newChar)
                else: 
                    currentIndex = Lowercase_Letters.index(i) + 1
                    remainingNumberOfLetters = 26 - currentIndex
                    newChar = Lowercase_Letters[args.s - remainingNumberOfLetters - 1]
                    cipherText.append(newChar)




    elif(args.f != None):
        path = args.f
        with open(path, "r") as file:
            for i in file:
                for char in i:
                    try:
                        if char.isupper(): # check if its an uppercase letter
                            index = Uppercase_Letters.index(char) # 
                            newChar = Uppercase_Letters[index + args.s]
                            cipherText.append(newChar)
                        else:
                            index = Lowercase_Letters.index(char)
                            newChar = Lowercase_Letters[index + args.s]
                            cipherText.append(newChar)
                    except:
                        if i.isupper(): # Check if its in lowercase
                            currentIndex = Uppercase_Letters.index(char) + 1
                            remainingNumberOfLetters = 26 - currentIndex
                            newChar = Uppercase_Letters[args.s - remainingNumberOfLetters - 1]
                            cipherText.append(newChar)
                        else: 
                            currentIndex = Lowercase_Letters.index(char) + 1
                            remainingNumberOfLetters = 26 - currentIndex
                            newChar = Lowercase_Letters[args.s - remainingNumberOfLetters - 1]
                            cipherText.append(newChar)
                
    print(''.join(cipherText))


main()
