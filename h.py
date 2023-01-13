import matplotlib.pyplot as akonPlotter

for i in range(1,5):
    akonData = {
        "Kagwapohan pag nasa EVSU": i,
        "Kagwapohan pag nasa Boarding house": 50,
        "Charm": 70,
        "Mapagmahal rate": 70,
        "Loyal rate": 100
    }

    subjects = list(akonData.keys())
    numberOfEnrollees = list(akonData.values())

    figure = akonPlotter.figure(figsize=(40,5))

    akonPlotter.bar(subjects, numberOfEnrollees, color = "blue", width=0.5)

    akonPlotter.xlabel("Criteria para Kay Shawn")
    akonPlotter.ylabel("Rating")
    akonPlotter.title("Rating ng Mga EVSU Student ni Shawn")
    akonPlotter.show()

# def digit_sum(n):
#     n = str(n)
#     sum = 0
#     for i in n:
#         sum += int(i)
#     return sum 

# def longest_word(text):
#     text = text.replace("\n", " ")
#     words = text.split(" ")
#     longestword = " "
#     for i in words:
#         if len(i) >= len(longestword):
#             print(i)
            
            
#     print()

# longest_word("The king is the current\nking")