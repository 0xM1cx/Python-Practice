from os import system, getcwd
from time import sleep
from string import ascii_uppercase, digits, punctuation
from MainAdmin import adminMode
from MainCustomer import customerMode
from InputCustomer import readInventoryReport
from ScreensStore import storeSign, storeSignAdmin, errorMessage



class Account:
    def __init__(self, username, password, address, contact_no):
        self.username = username
        self.password = password
        self.address = address
        self.contact_no = contact_no



account_list = []
purchase_list = []



def readAccountStorage(acc_storage):
    acc_list = []
    
    get_file_path = getcwd()
    
    create_file_path = f"{get_file_path}\\Text Files"
    
    read_acc_list = open(f"{create_file_path}\\account_list.txt", "r")
    read_account = read_acc_list.readline()

    while read_account != "":
        account_details = read_account.split()
        
        acc_list.append((account_details[0], account_details[1], account_details[2], account_details[3]))
        
        read_account = read_acc_list.readline()
        
    read_acc_list.close()
    
    acc_storage = acc_list
    
    return acc_storage



def writeAccountStorage(acc_storage):
    get_file_path = getcwd()
        
    create_file_path = f"{get_file_path}\\Text Files"
    
    write_acc_list = open(f"{create_file_path}\\account_list.txt", "w")
    
    for account_details in acc_storage:
        write_to_file = f"{account_details[0]} {account_details[1]} {account_details[2]} {account_details[3]}\n"
        
        write_acc_list.write(write_to_file)
        
    write_acc_list.close()



def login():
    global account_list
    
    if len(account_list) == 0:
        account_list = readAccountStorage(account_list)
        
    storeSign()
    print("     LOG-IN TO ShopSmart\n")
    print("=" * 30, "\n")
    print(' *Type -1 at the prompt to\n  cancel the process*\n')
    print("=" * 30, "\n\n")
    
    while True:
        username_input = input("\033[1A\033[K Enter Username: ")
        
        if username_input == "-1":
            return None
        elif username_input == "admin" or [un for un in account_list if un[0] == username_input]:
            break
        else:
            sleep(0.5)
            print("\033[1A\033[K      USER DOES NOT EXIST")
            sleep(1.25)
    
    print()
    
    while True:
        password_input = input("\033[1A\033[K Enter Password: ")
        
        if password_input == "-1":
            return None
        elif username_input == "admin" and password_input == "admin":
            adminMode()
            break
        elif [un for un in account_list if un[0] == username_input and un[1] == password_input]:
            customerMode(username_input)
            break
        else:
            sleep(0.5)
            print("\033[1A\033[K      INCORRECT PASSWORD")
            sleep(1.25)


def signup():
    global account_list
    
    account_list = []
    account_list = readAccountStorage(account_list)
        
    storeSign()
    print("   CREATE ShopSmart ACCOUNT\n")
    print("=" * 30, "\n")
    print("  Account Creation Guidelines\n")
    print(" - Usernames are permanent and\n   cannot be changed")
    print(" - Usernames must not contain\n   spaces or punctuation")
    print(" - Usernames must be at least\n  3 characters in length")
    print(" - Addresses must not contain\n   spaces or punctuation")
    print(" - Addresses must be at least\n  3 characters in length")
    print(" - Replace spaces with a dash\n   for addresses")
    print(" - Contact numbers must be 11\n   digits in length")
    print(" - Passwords must be at least\n   8 characters in length")
    print(" - Passwords must contain at\n   least 1 uppercase letter")
    print(" - Passwords must contain at\n   least 1 number\n")
    print("=" * 30, "\n")
    print(' *Type -1 at the prompt to\n  cancel the process*\n')
    print("=" * 30, "\n\n")
    
    while True:
        invalid_username = 0
        
        new_username = input("\033[1A\033[K Enter Username: ")
        
        if new_username == "-1":
            return None
        
        for i in new_username:
            if i in punctuation or i == " ":
                invalid_username += 1
                
        if invalid_username != 0 or len(new_username) < 3:
            sleep(0.5)
            print("\033[1A\033[K       INVALID USERNAME")
            sleep(1.25)
        elif new_username == "admin" or [un for un in account_list if un[0] == new_username]:
            sleep(0.5)
            print("\033[1A\033[K     USER ALREADY EXISTS")
            sleep(1.25)
        else:
            break
        
    print("\n")
    
    while True:
        invalid_address = 0
        
        new_address = input("\033[1A\033[K Enter Address: ")
        
        if new_address == "-1":
            return None
        
        for i in new_address:
            if i in [punc for punc in punctuation if punc != "-"] or i == " ":
                invalid_address += 1
                
        if invalid_address != 0 or len(new_address) < 3:
            sleep(0.5)
            print("\033[1A\033[K       INVALID ADDRESS")
            sleep(1.25)
        else:
            break
        
    print()
    
    while True:
        invalid_conact_no = 0
        
        new_contact_no = input("\033[1A\033[K Enter Contact #: ")
        
        if new_contact_no == "-1":
            return None
        
        for i in new_contact_no:
            if i not in digits:
                invalid_conact_no += 1
                
        if invalid_conact_no != 0 or len(new_contact_no) != 11:
            sleep(0.5)
            print("\033[1A\033[K       INVALID CONTACT #")
            sleep(1.25)
        elif [un for un in account_list if un[3] == new_contact_no]:
            sleep(0.5)
            print("\033[1A\033[K    CONTACT # ALREADY USED")
            sleep(1.25)
        else:
            break
    
    print("\n")
    
    while True:
        uppercase_true = 0
        numbers_true = 0
        
        new_password = input("\033[1A\033[K Enter Password: ")
        
        if new_password == "-1":
            return None
        
        for i in new_password:
            if i in ascii_uppercase:
                uppercase_true += 1
        
        for i in new_password:
            if i in digits:
                numbers_true += 1
                
        if uppercase_true != 0 and numbers_true != 0 and len(new_password) >= 8:
            break
        else:
            sleep(0.5)
            print("\033[1A\033[K       INVALID PASSWORD")
            sleep(1.25)
            
    print()
    
    while True:
        confirm_password = input("\033[1A\033[K Confirm Password: ")
            
        if confirm_password == "-1":
            return None
        
        if confirm_password == new_password:
            break
        else:
            sleep(0.5)
            print("\033[1A\033[K    PASSWORDS DON'T MATCH")
            sleep(1.25)
            
    storeSign()
    print("     NEW ACCOUNT OVERVIEW\n")
    print("=" * 30, "\n")
    print(f" Username: {new_username}\n")
    print(f" Address: {new_address.title()}")
    print(f" Contact #: {new_contact_no}\n")
    print(f" Password: {new_password}\n")
    print("=" * 30, "\n\n")
    
    while True:
        confirm_prompt = input("\033[1A\033[K Create Account? [Y/N]: ")

        if confirm_prompt.upper() in "YN" and len(confirm_prompt) == 1:
            break
        else:
            errorMessage()
            
    if confirm_prompt in "nN":
        return None
    
    storeSign()
    print(" SUCCESSFULLY CREATED ACCOUNT\n")
    print("=" * 30, "\n\n")
    
    new_account = Account(new_username, new_password, new_address.title(), new_contact_no)
    
    account_list.append((new_account.username, new_account.password, new_account.address, new_account.contact_no))
    
    writeAccountStorage(account_list)
    
    while True:
        login_prompt = input("\033[1A\033[K Proceed to Log-In? [Y/N]: ")

        if login_prompt.upper() in "YN" and len(login_prompt) == 1:
            break
        else:
            errorMessage()
        
    if login_prompt in "yY":
        login()
    


def customerList():
    global purchase_list
    global account_list
    
    purchase_list = []
    purchase_list = readInventoryReport(purchase_list)
    
    account_list = []
    account_list = readAccountStorage(account_list)
        
    storeSignAdmin()
    print("       CUSTOMER DATABASE\n")
    print("=" * 30)
    
    if len(account_list) == 0:
        print("\n        WOW SUCH EMPTY\n")
        print("=" * 30, "\n")
    else:
        for acc in account_list:
            products_purchased = 0
            total_paid = 0
            
            for purchase in purchase_list:
                if purchase[0] == acc[0]:
                    products_purchased += purchase[3]
                    total_paid += purchase[4]
                    
            print(f"\n          CUSTOMER # {account_list.index(acc) + 1}")
            
            print(f"Userame: {acc[0]}\n")
            print(f"Address: {acc[2]}")
            print(f"Contact #: {acc[3]}\n")
            print(f"Total Products Purchased: {products_purchased}")
            print(f"Total Amount Paid: PHP {total_paid:.2f}")
            
            if account_list.index(acc) != len(account_list) - 1:
                print("\n" + "-" * 30)
                
        print("\n" + "=" * 30, "\n")
        
    system("pause")