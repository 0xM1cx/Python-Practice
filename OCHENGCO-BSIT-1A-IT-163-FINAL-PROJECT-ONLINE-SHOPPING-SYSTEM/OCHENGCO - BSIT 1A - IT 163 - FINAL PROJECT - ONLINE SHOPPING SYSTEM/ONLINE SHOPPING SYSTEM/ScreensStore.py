from os import system
from time import sleep



def storeSign():
    system("cls")
    
    print("=" * 30)
    print("\n    - - - ShopSmart - - -\n")
    print("=" * 30, "\n")
    
    

def storeSignAdmin():
    system("cls")
    
    print("=" * 30)
    print("\n    - - - ShopSmart - - -\n")
    print("        (ADMIN MODE)\n")
    print("=" * 30, "\n")
    
    
    
def mainScreen():
    storeSign()
    
    print('"Clever Shopping Made Simple!"\n')
    print("=" * 30, "\n")
    print("\t[L] - LOG-IN")
    print("\t[S] - SIGN-UP")
    print("\t[X] - EXIT\n")
    print("=" * 30 + "\n\n")
    
    
    
def mainScreenAdmin():
    storeSignAdmin()
    
    print(" [P] - PRODUCT CENTER")
    print(" [C] - CUSTOMER DATABASE")
    print(" [I] - INVENTORY CENTER")
    print(" [X] - RETURN TO LOG-IN MENU\n")
    print("=" * 30 + "\n\n")
    
    
    
def productCenterScreen():
    system("cls")
    
    print("=" * 30)
    print("\n    - - - ShopSmart - - -\n")
    print("      (PRODUCT CENTER)\n")
    print("=" * 30, "\n")
    
    print(" [A] - ADD PRODUCTS")
    print(" [E] - EDIT PRODUCTS")
    print(" [V] - VIEW PRODUCTS")
    print(" [M] - RETURN TO ADMIN MENU\n")
    print("=" * 30 + "\n\n")
    
    
    
def editProductScreen():
    system("cls")
    
    print("=" * 30)
    print("\n    - - - ShopSmart - - -\n")
    print("      (PRODUCT CENTER)\n")
    print("=" * 30, "\n")
    print("       EDITING PRODUCT\n")
    print("=" * 30, "\n")
    
    
    
def inventoryCenterScreen():
    system("cls")
    
    print("=" * 30)
    print("\n    - - - ShopSmart - - -\n")
    print("     (INVENTORY CENTER)\n")
    print("=" * 30, "\n")
    
    print(" [I] - VIEW INVENTORY")
    print(" [P] - VIEW PURCHASE HISTORY")
    print(" [M] - RETURN TO ADMIN MENU\n")
    print("=" * 30 + "\n\n")
    
    
    
def productCreationGuidelines():
    print("  Product Creation Guidelines\n")
    print(" - Product names are permanent\n   and cannot be changed")
    print(" - Product names must not\n   contain spaces or\n   punctuation")
    print(" - Product names must be at least\n   3 characters in length")
    print(" - Replace spaces with a dash\n")
    print("=" * 30, "\n")
    
    
    
def mainScreenCustomer(un):
    storeSign()
    
    print(f"Shop Smartly [{un}]!\n")
    print("=" * 30, "\n")
    print(" [B] - BUY PRODUCTS")
    print(" [V] - VIEW PRODUCTS")
    print(" [H] - PURCHASE HISTORY")
    print(" [E] - ACCOUNT CENTER")
    print(" [X] - LOG-OUT\n")
    print("=" * 30 + "\n\n")
    
    
    
def logOutScreen():
    storeSign()
    
    print("         LOGGING OUT\n")
    print("=" * 30, "\n\n")



def errorMessage():
    sleep(0.5)
    print("\033[1A\033[K        INVALID INPUT")
    sleep(1.25)