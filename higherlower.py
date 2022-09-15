import random

def higherLower():
    '''Create a program where the player will guess the exact positive integer the bot is holding'''
    botNumber = random.randint(0, 1000)
    nTurns = 0
    answerStatus = True
    try:
        while answerStatus:
            playerInput = int(input("Your Guess: "))
            if playerInput > botNumber:
                print("Lower")
                nTurns += 1
            elif playerInput < botNumber:
                nTurns += 1
                print("Higher")
            else:
                print(f"Correct! You guessed the correct answer in {nTurns} turns")
                answerStatus = False
    except:
        print("Input must be an Integer")

higherLower()

    
        
    
