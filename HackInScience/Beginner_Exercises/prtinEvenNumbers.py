def print_even_numbers(start, stop):
    '''Write a function printing every even numbers in the given range, 
    one number per line.'''

    for i in range(start, stop):
        if i % 2 == 0:
            print(i)


def sumOfEvenNumbers():
    '''Provide a script that prints the sum of every 
    even numbers in the range [0; 100].'''
    sum = 0
    for i in range(0, 101):
        if i % 2 == 0:
            sum += i
    return sum 