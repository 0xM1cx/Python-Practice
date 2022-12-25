# Day 1 of python review

## Arbitrary number of arguments

def main(*ages):
    for i in ages:
        print(i)

    print("----------------")

    for b in range(0, len(ages)):
        print(ages[b])


# main(1, 2, 3, 4, 5, 6, 7, 7, 8)


## Lambda Function Practice
birthYear = int(input())
user_age = lambda birthYear : 2022 - birthYear
print(f"You are now {user_age(birthYear)} years old")