#Sudaria, Shawn Michael A.

record = []

def Add_Records(record):
    print("\nAddding a Record\n")
    uInput = input("E.g Name Year Section:  ")
    uInput = uInput.split(" ")
    stud_rec = f"{uInput[0]} - {uInput[1]} - {uInput[2]}"
    record.append(stud_rec)


def View_Records(record):
    print("\nList of Records\n")
    num = 1
    for stud in record:
        print(f"{num}.",stud)
        num += 1
  
def Edit_Records(record):
    print("\nEdit Records\n")
    View_Records()

    index = int(input("CHOICE by index:  ")) - 1
    
    #edit dd na part
    new_item = input("New Item(e.g Name Year Section): ")
    new_item = new_item.split(" ")
    record[index] = f"{new_item[0]} - {new_item[1]} - {new_item[2]}"

    
def Delete_Records(record):
    print("\nDelete a Record\n")
    View_Records()

    index = int(input("Choose what to delete: ")) - 1
    del record[index]

    

    
    
def Exit_Records():
    print("Are you sure you want to exit?")



def System_Menu():
    print("System Menu")
    print("[ A ] - Add Record")
    print("[ E ] - Edit Record")
    print("[ D ] - Delete Record")
    print("[ V ] - View Record")
    print("[ X ] - Exit Record")
    userInput = input("Choice: ")

    if userInput.upper() == "A":
        Add_Records(record)
        System_Menu()
    elif userInput.upper() == "E":
        Edit_Records(record)
        System_Menu()
    elif userInput.upper() == "D":
        Delete_Records(record)
        System_Menu()
    elif userInput.upper() == "V":
        View_Records(record)
        System_Menu()
    elif userInput.upper() == "X":
        Exit_Records()


    

System_Menu()

