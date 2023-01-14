def dist(arr):
    greatestVal = max(arr)
    lowestVal = min(arr)
   
    if greatestVal < 0 and lowestVal < 0:
        return greatestVal - lowestVal
    elif greatestVal < 0 or lowestVal < 0:
        return abs(lowestVal) + abs(greatestVal);
    else:
        return greatestVal - lowestVal

print(dist([-1, -2, -3]))
