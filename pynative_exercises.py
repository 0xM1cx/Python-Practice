def exerciseOne():
    '''print pyramid number'''
    for i in range(10):
        for j in range(i):
            print(i, end=" ")
        print()


def exerciseTwo():
    '''Calculate the sum of all numbers from 1 to a given 
    number'''
    sum = 0
    givenNumber = input("Give a number: ")
    for i in range(1, int(givenNumber) + 1):
        sum += i
    return sum

def exerciseThree():
    '''Write a program to print multiplication table of a given number'''
    n = input("Give a number: ")
    for i in range(1, 11):
        print(int(n) * i)

def exerciseFour():
    '''Write a program to display those numbers from a list that will satisfy the following
    conditions

    * The number must be divisible by five
    * If the number is greater than 500, then stop the loop.'''
    arr = []
    bool = True
    while bool:
        Userinput = int(input("Number: "))

        if Userinput % 5 == 0 and Userinput < 500 and Userinput < 150:
            arr.append(Userinput)
            continue
        elif Userinput > 150 and Userinput < 500:
            continue
        elif Userinput > 500:
            bool = False
    print(arr)

def exerciseFive():
    UserInput = int(input("Range: "))
    for i in range(UserInput, 0, -1):
        for b in range(i, 0, -1):
            print(b, end=" ")
        print()

def exerciseSix():
    UserInput = input("Numbers: ")
    numbers = UserInput.split(" ")
    currentIndex = len(numbers)
    for i in range(len(numbers)):
        print(numbers[currentIndex - 1])
        currentIndex -= 1

