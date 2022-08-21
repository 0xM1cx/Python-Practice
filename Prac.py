'''
In this problem, you will write a program that reads words from the user until the user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in the same order that they were entered. 
For example, if the user enters:
first
second
first
third
second
then your program should display:
first
second
third
'''



UserInput = str(input("Type Here: "))
Inputs = []
while UserInput:
    if UserInput not in Inputs:
        Inputs.append(UserInput)
    UserInput = str(input("Type Here: "))
    

for i in Inputs:
    print(i)


