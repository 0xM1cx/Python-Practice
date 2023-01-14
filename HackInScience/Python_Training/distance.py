def getDistance(arr):
    greatestVal = max(arr)
    lowestVal = min(arr)

    if greatestVal < 0 or lowestVal < 0:
        return lowestVal + greatestVal;
    else:
        return greatestVal - lowestVal


print(getDistance([1, 2, 3]))
