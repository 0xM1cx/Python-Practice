# Program 1
def findLargestNumber():
    '''Find the largets number of the array of numbers'''
    arr = [int(i) for i in input().split(" ")]
    currentLargestNumber = 0
    for i in arr:
        for b in arr:
            if i > b:
                currentLargestNumber = i
            else:
                currentLargestNumber = b


    print(f"The largest number in the array is: {currentLargestNumber}")

#Program 2
def findLargestString():
    '''Find the word with the largest length'''
    words = [str(i) for i in input().split(" ")]
    currentLargestWord = ''
    for i in words:
        for b in words:
            if len(i) > len(b):
                currentLargestWord = i
            else:
                currentLargestWord = b

    print(f"The largest word in the array is: {currentLargestWord}")

