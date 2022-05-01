from sys import argv
'''
Write a program that do basic calculations.
You need to be able to get basic operators such as +, - , *, /, % (modulo) and ^ (Exponentiation). Input will be integer numbers.
Your program will give a usage message if you don't give the three parameters.
For every other errors like if an operand is not an integer, you'll print an input error.
'''

try:
    if argv[2] == "+":
        print(int(argv[1]) + int(argv[3]))
    elif argv[2] == "-":
        print(int(argv[1]) - int(argv[3]))
    elif argv[2] == "*":
        print(int(argv[1]) * int(argv[3]))
    elif argv[2] == "/":
        print(int(argv[1]) / int(argv[3]))
    elif argv[2] == "%":
        print(int(argv[1]) % int(argv[3]))
    elif argv[2] == "^":
        print(int(argv[1]) ** int(argv[3]))
    elif len(argv) < 4:
        print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
    elif "+" or "-" or "*" or "/" or "%" or "^" not in argv:
        print("input error")
except IndexError:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")

except ZeroDivisionError:
    print("input error")






## SOMEONE ELSE'S CODE
## READ TO COMPARE AND LEARN

import sys
import operator

if len(sys.argv) != 4:
    print('usage: ./solution.py a_number (an_operator +-*/%^) a_number')
    exit()

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.pow,
}

a, op, b = sys.argv[1:]

try:
    a = int(a)
    b = int(b)
    print(ops[op](a, b))
except:
    print('input error')



