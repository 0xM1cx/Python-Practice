import string


letters = string.ascii_letters

rucksacks = []
duplicates = []

with open("./input.txt", "r") as f:
    for i in f:
        removedNewline = i.replace("\n", "")
        rucksacks.append(removedNewline)
sample = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]

def findSum(duplicates, sum):
    for i in duplicates:
        sum += letters.index(i)+1
    
    return sum


def findDuplicates(array):
    sumOfDuplicates = 0
    for j in array:
        mean = len(j)//2
        for f_half in j[0:mean]:
            for s_half in j[mean:len(i)]:
                if f_half == s_half and f_half not in duplicates:
                    duplicates.append(f_half)
                else:
                    continue
        sumOfDuplicates = findSum(duplicates, sumOfDuplicates)
        duplicates.clear()

    print(sumOfDuplicates)



findDuplicates(rucksacks)


