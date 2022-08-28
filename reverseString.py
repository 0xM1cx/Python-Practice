# Reverse a string
UserInput = input("String: ")
def reverseString(INPUT):
    charArr = list(INPUT)
    reversed = []
    arrlen = len(charArr)
    for i in range(len(charArr)):
        arrlen -=  1
        reversed.append(charArr[arrlen])

    print("".join(reversed))


reverseString(UserInput)



