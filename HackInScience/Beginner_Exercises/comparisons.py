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


biggestNumber = 0
for i in the_list:
    for b in the_list:
        if i > b:
            biggestNumber = i

print(biggestNumber)