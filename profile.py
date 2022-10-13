class Person:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def getFullName(self, numArg):
        if numArg == 0:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        elif numArg == 1:
            return f"{self.last_name}, {self.first_name} {self.last_name}"

P1 = Person("Shawn Michael", "Abbang", "Sudaria")

print(P1.getFullName(1))
print(P1.getFullName(0))

        
