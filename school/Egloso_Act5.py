# Account Authentication Simulation

usernames= ["John", "Alenere", "David"]
passwords = ["abc123", "123abc", "a1b2c3"]


U_Input = input("Username: ")
P_Input = input("Password: ")

for Uname in usernames:
    if U_Input == Uname:
        if P_Input == passwords[usernames.index(U_Input)]:
            print(f"Welcome {U_Input}")
        else:
            print("Account Not Found")
    else:
        print("Account Not Found")