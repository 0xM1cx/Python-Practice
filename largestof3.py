'''Create a program, that accepts three integers. Compare each and print the largest value among the three'''


def assignmentTwo():
    '''Create a simple program, that accepts three integers. Compare each and print the largest value among the three.'''
    numArray = []
    for i in range(3):
        integer = int(input("Number: "))
        numArray.append(integer)
    biggestNumber = 0
    for i in numArray:
        for b in numArray:
            if i > b:
                biggestNumber = i

    print(f"The biggest number is {biggestNumber}")


