'''
Write a function named from_roman_numeral that return the value of a given roman numeral.
'''
romanNumeral_ToInt = {
        "I": 1,
        "V": 5, 
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

user_input = input()
def from_roman_numeral(user_input, dic):
    n = 0
    try:
        UInput = user_input.split("")
    except:
        UInput = user_input

  

    for i in UInput:
        n += int(dic[i])
        
    print(n)



from_roman_numeral(user_input, romanNumeral_ToInt)