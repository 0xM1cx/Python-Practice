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

n = str(input("RN: "))

def from_roman_numeral(roman_numeral):
    sum = 0
    if roman_numeral == "CD":
        sum += 400
    elif roman_numeral == "XL":
        sum += 40
    else:
        for i in roman_numeral:
            sum += int(romanNumeral_ToInt[i])
    return sum

print(from_roman_numeral(n))