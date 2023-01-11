


numOfOverlaps = 0
pairs = []

def getNumberOfOverlaps(pairs, numOfOverlaps):
    for item in pairs:
        for subItem in item:
            if subItem in pairs[1]:
                numOfOverlaps += 1
                break

    return numOfOverlaps


with open(".\input4Day4.txt", "r") as file:
    for line in file:
        removedNewLine = line.replace("\n", "")
        currentGroup = removedNewLine.split(",")
        for pair in currentGroup:
            pairs.append(pair.split("-"))

        numOfOverlaps = getNumberOfOverlaps(pairs, numOfOverlaps)
        pairs.clear()


print(numOfOverlaps)




