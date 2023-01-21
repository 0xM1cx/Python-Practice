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
        uInput = input().split(' ')
        uInput = [int(x) for x in uInput]
        testCaseWorth = uInput[0] // 10
        print(testCaseWorth * uInput[1])
    
def kitchenTimings():
    '''The working hours of Chef's kitchen are from X pm to Y pm
    (1 <= x <= Y <= 12). Find the number of hours chef works'''

    testCases = int(input())
    for i in range(testCases):
        uInput = input().split(' ')
        uInput = [int(x) for x in uInput]
        print(uInput[1] - uInput[0])



def TaxInChefland():
    '''In Chefland, a tax of 10 rupees is deducted if the total income
    is strictly greater than 100 rupees. Given the total income is X
    rupees, find out how much money you get.'''

    testCases = int(input())
    for i in range(testCases):
        uInput = int(input())
        if uInput > 100:
            print(uInput - 10)
        else:
            print(uInput)


def AudibleRange():
    '''Chef's dog binary hears frequencies starting from 67 Hertz to 
    45000 Hertz (both inclusive). If Chef's commands have a frequency
    of X Hertz, find whether binary can hear them or not.'''

    testCases = int(input())

    for i in range(testCases):
        uInput = int(input())
        if uInput >= 67 and uInput <= 45000:
            print("YES")
        else:
            print("NO")
    
def ReachOnTime():
    '''It takes 30 mins for Chef to reach office from the apartment.
    Chef left for the office X minutes before Chef was supposed to reach.
    Determine whether or not Chef will be able to reach on time.'''

    testCase = int(input())
    for i in range(testCase):
        uInput = int(input())
        if uInput >= 30:
            print("YES")
        else:
            print("NO")
    



def WhoIsTaller():
    '''Charlie measured the heights of Alice and Bob, and got to know that
    Alice's height is X centimeters and Bob's height is Y centimeters. 
    Help Charlie decide who is taller'''
    
    testCases = int(input())
    for i in range(testCases):
        uInput = input().split(' ')
        uInput = [int(x) for x in uInput]

        if uInput[0] > uInput[1]:
            print("A")
        else:
            print("B")
        
def ReachTheTarget():
    '''There is a cricket match going on between team A and B. Team B
    is batting secodn and got a target of X runs. Currently, team B has
    scored Y runs. Determine how many more runs Team B should score to
    win the match.'''

    testCase = int(input())

    for i in range(testCase):
        uInput = input().split(' ')
        uInput = [int(x) for x in uInput]

        print(uInput[0] - uInput[1])

def TourOfKing():
    '''King has N  cars that can seat 5 people eachh and M cars that can
    seat 7 people each. Determine the maximum number of people that can
    travel together in these cars'''
    testCases = int(input())
    for i in range(testCases):
        uInput = input().split(' ')
        uInput = [int(x) for x in uInput]
        print((uInput[0] * 5)+(uInput[1] * 7))