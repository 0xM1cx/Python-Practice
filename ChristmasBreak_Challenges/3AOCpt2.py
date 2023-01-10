import string

## This is part of the Adven Of Code challenge Day 3

letters = string.ascii_letters

rucksacks = []
badges = []

group = []

badge_priority = []

with open("./input.txt", "r") as f:
    for i in f:
        removedNewline = i.replace("\n", "")
        rucksacks.append(removedNewline)
sample = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]




def getCommonBadge():
    for i in group[0]:
        if i in group[1]:
            if i in group[2]:
                return i
        else:
            continue
    

def findGroup(array):
    counter = 0
    while counter < len(array):
        # get the first 3 lines
        for j in range(len(array)):
            group.append(array[counter])
            counter += 1
            if counter % 3 == 0:
                break

        groupCommonBadge = getCommonBadge()
        print(groupCommonBadge)
        badge_priority.append(letters.index(groupCommonBadge)+1)
        group.clear()
    
    

    



findGroup(rucksacks)
print(sum(badge_priority))

