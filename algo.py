# Program 1


def findLargestNumber():
    '''Find the largets number of the array of numbers'''
   # arr = [int(i) for i in input().split(" ")]
    arr = [9276863257, 9752587452, 9812367549, 9126745397, 9623837625, 9812574829, 9124762985, 9351865836, 9752749873, 97124568732, 9673245763, 9865746352, 9812356748, 9346527986, 9783516368, 9851374859, 9812345685, 9835245742] 
    currentLargestNumber = 0
    for i in arr:
        for b in arr:
            if i > b:
                currentLargestNumber = i
            else:
                currentLargestNumber = b


    print(f"The largest number in the array is: {currentLargestNumber}")
findLargestNumber()
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

