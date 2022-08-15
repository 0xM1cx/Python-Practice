the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]

# The for loop below goes through every element 
# in the list and compares that element to the biggestNumber variable
# if the element is greater than the biggestNumber variable then it replaces its value
# with the value of i which is the current element on the lsit that is passed.

biggestNumber = 0
for i in the_list:
    if i > biggestNumber:
        biggestNumber = i

print(biggestNumber)