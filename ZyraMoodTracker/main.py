def AddLog():
    pass

def EditTodayLog():
    pass

def EditSpecificLog():
    pass

def ViewLogs():
    pass


def main():
    print("""MOOD TRACKER
    [1] Add a Today's Log
    [2] Edit Today's Log
    [3] Edit a Specific Log
    [4] View Logs
    """)
    choice = int(input("What do you want to do: "))

    if choice == 1:
        AddLog()
    elif choice == 2:
        EditTodayLog()
    elif choice == 3:
        EditSpecificLog()
    elif choice == 4:
        ViewLogs()
    


main()