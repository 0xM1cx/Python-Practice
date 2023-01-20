def BaynariClasses():
    testCases = input()
    for i in range(int(testCases)):
        uInput = input().split(' ')
        print(int(uInput[0]) * int(uInput[1]))


def Fitness():
    testCases = int(input())
    for i in range(testCases):
        xKilometers = int(input())
        print(xKilometers * 10) 


def Ludo():
    testCases = int(input())
    for i in range(testCases):
        rollNumber = int(input())
        if rollNumber == 6:
            print("YES")
        else:
            print("NO")

def Burgers():
    testCases = int(input())
    for i in range(testCases):
        ingredients = input().split(' ')
        converted = [int(x) for x in ingredients]
        print(min(converted)) 


Burgers()



