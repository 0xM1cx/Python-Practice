def displayNumberPyramid(): # Problem Complete
    rowInput = str(input())
    for i in range(int(rowInput) + 1):
        for j in range(i):
            print(i, end=" ")
        print("")

def displayNumberColumns(): # Problem Complete
    numberRange = input("Number range: ")
   
    for j in range(1, int(numberRange) + 1):
        if j % 5 == 0:
            print(j)
            continue
        print(j, end="\t")


def displayUpsideDownPyramid(): # Problem Completed
    for i in range(11, 0, -1):
        for j in range(i):
            print("*", end="")
        print("")
    for i in range(0, 11):
        for j in range(i):
            print("*", end="")
        print("")

def sumOfPrevAndCurrent(): 
    '''Write a program to iterate the first 10 numbers and
    in each iteration, print the sum of the current and previous 
    number. '''
    previousNumber = 0
    for i in range(0,10):
        sum = i + previousNumber
        print(f"Current Number {i} Previous Number {previousNumber} Sum: {sum}")
        previousNumber -= 1
    
    
def numberPyramidReversed(): # Problem Completed
    for i in range(6, 0, -1):
        for j in range(i):
            print(j, end=' ')
        print("")

def spacedPyramid():
    for i in range(11):
        for b in range(i):
            print("*", end=" ")
        print("")

displayNumberColumns()
