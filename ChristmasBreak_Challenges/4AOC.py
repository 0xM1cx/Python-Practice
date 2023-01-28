fullyContain = 0

def getNumOfFullyContained(firstPair, secondPair):
    noOfContained = 0
    for item in firstPair:
        if item in secondPair:
            noOfContained += 1

    if noOfContained == len(firstPair) or noOfContained == len(secondPair):
        global fullyContain
        fullyContain += 1

def separateSections(sectionOne, sectionTwo):
    firstPair = []
    secondPair = []

    # Section 1
    for i in range(int(sectionOne[0]), int(sectionOne[1]) + 1):
        firstPair.append(i) 

    # #Section 2
    for x in range(int(sectionTwo[0]), int(sectionTwo[1]) + 1):
        secondPair.append(x)

    getNumOfFullyContained(firstPair, secondPair)
    


with open(".\input4Day4.txt", "r") as file:
    for line in file:
        removedNewLine = line.replace("\n", "")
        currentGroup = removedNewLine.split(",")

        first_index = currentGroup[0].split("-")
        second_index = currentGroup[1].split("-")

        sectionOne = []
        sectionTwo = []


        for b in first_index:
            sectionOne.append(b)
        for a in second_index:
            sectionTwo.append(a)
        numOfOverlaps = separateSections(sectionOne, sectionTwo)



print(fullyContain)




