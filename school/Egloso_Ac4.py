Math_ques_str = ["1+2", "10+4", "100-49", "10000 + 6"]
Math_ques = [1+2, 10+4, 100-49, 10000 + 6]

no_attempts = 3
for item in Math_ques_str:
    no_attempts -= 1
    if no_attempts == 0:
        break

    U_Answer = int(input("Answer: "))
    if U_Answer == Math_ques[Math_ques_str.index(item)]:
        print("Correct")