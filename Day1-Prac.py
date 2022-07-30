# Day 1 Practice Exercises
# All the question can be found here: https://www.w3resource.com/python-exercises/python-basic-exercises.php

import sys
from datetime import datetime
from math import pi

def questionOne():
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp Above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

def questionTwo():
    '''Write a Python program to get the Python version you are using'''
    print(sys.version_info)


def questionThree():
    '''Write a Python program to display the current date and time.'''
    print(datetime.now())

def questionFour():
    '''Write a Python program which accepts the radius of a circle from the user and compute the area. '''
    r = int(input("Radius: "))
    print(f"The area of the circle given {r} as radius is {round(pi * (r**2), 2)}")




