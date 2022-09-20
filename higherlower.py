import random

def assignmentThree():
    for i in range(10):
        for b in range(i):
            print('❤️',end="")
        print("")
    print("Nicole")
    for a in range(10, 1, -1):
        for k in range(a, 1, -1):
            print('❤️', end='')
        print("")

def assignmentTwo():
    '''Create a simple program, that accepts three integers. Compare each and print the largest value among the three.'''
    numArray = []
    for i in range(3):
        integer = int(input("Number: "))
        numArray.append(integer)
    biggestNumber = 0
    for i in numArray:
        for b in numArray:
            if i > b:
                biggestNumber = i

    print(f"The biggest number is {biggestNumber}")

def higherLower():
    '''Create a program where the player will guess the exact positive integer the bot is holding'''
    botNumber = random.randint(0, 1000)
    nTurns = 4
    answerStatus = True
    try:
        while answerStatus and nTurns:
            playerInput = int(input("Bot: Guess the correct answer...\nYour answer: "))
            if playerInput > botNumber:
                print("Bot: Lower!\n")
                nTurns -= 1
            elif playerInput < botNumber:
                print("Bot: Higher!\n")
                nTurns -= 1
            else:
                print(f"Correct! You guessed the correct answer in {nTurns} turns")
                answerStatus = False

        print("Bot: No more turns left")
    except:
        print("Input must be an Integer")


assignmentThree()

