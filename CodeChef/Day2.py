def unattemptedProblems():
    '''Our chef is currently practicing on CodeChef and is a begginer.
    The cout of "All Problems" in the beginner section is X. Our Chef
    has already "Attempted" Y problems among them. How many problems 
    are yet 'Un-attempted?'''

    uInput = input().split(' ')
    uInput = [int(x) for x in uInput]
    if uInput[1] >= 1 and uInput[0] >= uInput[1] and uInput[0] <= 1000:
        print(uInput[0] - uInput[1])
    
def determineScore():
    '''There is a problem worth X points. Chef finds out that the problem
    has exactly 10 test cases. It is known that each test case is worth
    the same number of points. Chef passes N test cases among them.
    Determine the score Chef will get.'''

    testCases = int(input())
    for i in range(testCases):
        pass

    

determineScore()