from sys import argv
'''
Write a program that prints the result of simple addition.

If no parameters are given, you must print the following error messasge:
usage: python3 solution.py OP1 OP2

'''

try:
    print(f"sum is {int(argv[1]) + int(argv[2])}")
except IndexError:
    print("usage: python3 solution.py OP1 OP2")