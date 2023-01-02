import random
import string

passSize = int(input("What is the length of the password? "))
print("What combinations will you password have?")
print("If you want uppercase letters type U, lowercase letters type l, digits with d and special characters with s")
print("Example input: s")


lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = "!@#$%^&*"

password = ""
for i in range(passSize):
    password.append()