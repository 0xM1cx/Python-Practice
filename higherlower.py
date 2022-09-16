import random

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


higherLower()

