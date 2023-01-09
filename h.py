# import matplotlib.pyplot as akonPlotter


# akonData = {
#     "Math": 40,
#     "Physics": 50,
#     "Chemistry": 40,
#     "Computer Science": 70,
#     "Philosophy": 50
# }

# subjects = list(akonData.keys())
# numberOfEnrollees = list(akonData.values())

# figure = akonPlotter.figure(figsize=(10,5))

# akonPlotter.bar(subjects, numberOfEnrollees, color = "blue", width=0.5)

# akonPlotter.xlabel("Mga subjects")
# akonPlotter.ylabel("Mga Number of Enrollees")
# akonPlotter.title("Number of students enrolled in sample courses")
# akonPlotter.show()

def digit_sum(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum 

def longest_word(text):
    text = text.replace("\n", " ")
    words = text.split(" ")
    longestword = " "
    for i in words:
        if len(i) >= len(longestword):
            print(i)
            
            
    print()

longest_word("The king is the current\nking")