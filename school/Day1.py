# Day 1 of python review
from math import sqrt
## Arbitrary number of arguments

def main(*ages):
    for i in ages:
        print(i)

    print("----------------")

    for b in range(0, len(ages)):
        print(ages[b])


# main(1, 2, 3, 4, 5, 6, 7, 7, 8)


## Lambda Function Practice
# birthYear = int(input())
# user_age = lambda birthYear : 2022 - birthYear
# print(f"You are now {user_age(birthYear)} years old")

# name = "Shawn"


# def testOUt():
#     f = user_age(birthYear)
    
#     global name

#     print(name)
    
#     name = "Crystal"
#     print(name)




raw_data = input("INPUT YOUR DATA: ").split(" ")
converted_data = [int(x) for x in raw_data]
x_bar = 0
def getStandardDeviation(data):
    global x_bar
    x_bar = sum(data) / len(data)
    result = 0
    for i in data:
        result += ((i - x_bar)**2)
    s_dev = result / (len(data) - 1)

    return round(sqrt(s_dev), 2)

print(f"The stadard Deviation of the given data is {getStandardDeviation(converted_data)}")
print(f"The average of the data is {x_bar}")