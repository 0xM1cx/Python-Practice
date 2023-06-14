from AccountCenter import login, signup
from ScreensStore import storeSign, mainScreen, errorMessage



def main():
    mainScreen()
    
    while True:
        choice = input("\033[1A\033[K Choice: ")

        if choice.upper() in "LSX" and len(choice) == 1:
            break
        else:
            errorMessage()
            
    if choice in "lL":
        login()
    elif choice in "sS":
        signup()
    elif choice in "xX":
        exitProgram()
        
    main()

    
    
def exitProgram():
    storeSign()
    
    print("       EXITING ShopSmart\n")
    print("=" * 30, "\n\n")
    
    while True:
        exit_prompt = input("\033[1A\033[K Are you sure? [Y/N]: ")

        if exit_prompt.upper() in "YN" and len(exit_prompt) == 1:
            break
        else:
            errorMessage()

    if exit_prompt in "yY":
        storeSign()
        
        print("  THANK YOU FOR SHOPPING AT\n    - - - ShopSmart - - -\n")
        quit("=" * 30)
    elif exit_prompt in "nN":
        main()
    
    
    
main()