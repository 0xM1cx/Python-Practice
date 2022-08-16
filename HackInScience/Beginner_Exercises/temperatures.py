# Write functions to convert from Fahrenheit to Celsius and vice-versa.

from time import process_time_ns


def fahrenheit_to_celsius(temp):
    F = temp
    C = (F - 32) * 5 / 9
    return C

def celsius_to_fahrenheit(temp):
    C = temp
    F = (C * 9/5) + 32
    return F

print(fahrenheit_to_celsius(98.6))
print(celsius_to_fahrenheit(26))