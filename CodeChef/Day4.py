def BullOrBear():
    '''Given that Chef bought the stock at value X and sold it at value Y.
    Help him calculate wheter he made a profit, loss, or was it neutral deal
    '''
    testCases = int(input())
    for b in range(testCases):
        uInput = input().split(" ")
        
        if int(uInput[0]) > int(uInput[1]):
            print("LOSS")
        elif int(uInput[0]) < int(uInput[1]):
            print("PROFIT")
        else:
            print("NEUTRAL")
        

BullOrBear()