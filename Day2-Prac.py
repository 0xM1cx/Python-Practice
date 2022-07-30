# All the questions can be found here: https://www.w3resource.com/python-exercises/python-basic-exercises.php

import sys

def questionFive():
    '''Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.'''
    firstName = input("FirstName: ")
    lastName = input("LastName: ")
    print(f"{lastName} {firstName}")

def questionSix():
    '''Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers'''
    listOfNumbers = sys.argv[1:]
    print(listOfNumbers)
    print(tuple(listOfNumbers))

def questionSeven():
    '''Write a Python program to accept a filename from the user and print the extension of that'''
    # Getting the file extension of this file
    extension = sys.argv[0].split(".")
    print(f"The extension the name of this file({sys.argv[0]}) is {extension[1]}")
    
    # Getting the file extension of the filename given by the user
    filename = input("filename you want: ")
    filext = filename.split(".")
    print(f"The extension of the filename({filename}) you entered is {filext[1]}")

def questionEight():
    '''Write a Python program to display the first and last colors from the following list.'''
    colors = input("Colors: ")
    colorList = colors.split(" ")
    print(colorList)

