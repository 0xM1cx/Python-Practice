from os import system
import AccountCenter as AC
from InputAdmin import readProductStorage, writeProductStorage
from InputCustomer import productNumber, orderQuantity, paymentAmount, AddressInput, ContactNoInput, PasswordInput, readInventoryReport, writeInventoryReport
from ScreensStore import storeSign, mainScreenCustomer, logOutScreen, errorMessage



product_list = []
purchase_history = []
account_storage = []



def customerMode(username):
    global product_list
    global purchase_history
    global account_storage
    
    product_list = []
    product_list = readProductStorage(product_list)
        
    purchase_history = []
    purchase_history = readInventoryReport(purchase_history)
        
    account_storage = []
    account_storage = AC.readAccountStorage(account_storage)
    
    mainScreenCustomer(username)
    
    while True:
        choice = input("\033[1A\033[K Choice: ")

        if choice.upper() in "BVHEX" and len(choice) == 1:
            break
        else:
            errorMessage()
            
    if choice in "bB":
        buyProduct(username)
        writeProductStorage(product_list)
        writeInventoryReport(purchase_history)
    elif choice in "vV":
        viewProduct()
        system("pause")
    elif choice in "hH":
        purchaseHistory(username)
    elif choice in "eE":
        editAccount(username)
        AC.writeAccountStorage(account_storage)
    elif choice in "xX":
        logOutScreen()
        
        while True:
            exit_prompt = input("\033[1A\033[K Are you sure? [Y/N]: ")

            if exit_prompt.upper() in "YN" and len(exit_prompt) == 1:
                break
            else:
                errorMessage()

        if exit_prompt in "yY":
            return None
        elif exit_prompt in "nN":
            pass
    
    customerMode(username)
    
    
    
def buyProduct(un):
    account_index = [acc[0] for acc in account_storage].index(un)
    account_details = account_storage[account_index]
    
    viewProduct()
    print("       BUYING PRODUCTS\n")
    print("=" * 30, "\n")
    print(' *Type "-1" at the prompt\n  to return to main menu*\n')
    print("=" * 30, "\n\n")
        
    new_order = orderInput()
    
    if new_order == None:
        return None
    
    payment_details = paymentInput(new_order)
    
    new_receipt = receipt(un, new_order, payment_details)
    
    purchase_history.append(new_receipt)

    updated_stock = editStock(new_receipt)
    
    product_list[new_order[0] - 1] = updated_stock
    
    storeSign()
    print("       PURCHASE RECEIPT\n")
    print("=" * 30, "\n")
    print(f" USERNAME: {new_receipt[0]}\n")
    print(f" ADDRESS: {account_details[2]}")
    print(f" CONTACT #: {account_details[3]}\n")
    print(f" PRODUCT NAME: {new_receipt[2]}")
    print(f" PRODUCT PRICE: PHP {product_list[new_receipt[1] - 1][1]:.2f}\n")
    print(f" QUANTITY: {new_receipt[3]}\n")
    print(f" ORDER TOTAL: PHP {new_receipt[4]:.2f}\n")
    print(f" AMOUNT PAID: PHP {new_receipt[5]:.2f}")
    print(f" CHANGE RECEIVED: PHP {new_receipt[6]:.2f}\n")
    print("=" * 30, "\n")

    system("pause")
    
    
    
def viewProduct():
    storeSign()
    print("       VIEWING PRODUCTS\n")
    print("=" * 30)
    
    if len(product_list) == 0:
        print("\n        WOW SUCH EMPTY\n")
        print("=" * 30, "\n")
    elif len(product_list) != 0:
        for prod in product_list:
            print(f"\n          PRODUCT # {product_list.index(prod) + 1}")
            
            print(f"Product Name: {prod[0]}")
            print(f"Product Price: PHP {prod[1]:.2f}")
            print(f"Amount in Stock: {prod[2]}")
            
            if product_list.index(prod) != len(product_list) - 1:
                print("\n" + "-" * 30)
                
        print("\n" + "=" * 30, "\n")
    
    
    
def purchaseHistory(un):
    account_purchase = [order for order in purchase_history if order[0] == un]
    
    storeSign()
    print("       PURCHASE HISTORY\n")
    print("=" * 30)
    
    if len(account_purchase) == 0:
        print("\n        WOW SUCH EMPTY\n")
        print("=" * 30, "\n")
    elif len(product_list) != 0:
        for order in account_purchase:
            print(f"\n          PURCHASE # {account_purchase.index(order) + 1}")

            print(f" PRODUCT NAME: {order[2]}")
            print(f" PRODUCT PRICE: PHP {order[4] / order[3]:.2f}\n")
            print(f" QUANTITY: {order[3]}\n")
            print(f" ORDER TOTAL: PHP {order[4]:.2f}\n")
            print(f" AMOUNT PAID: PHP {order[5]:.2f}")
            print(f" CHANGE RECEIVED: PHP {order[6]:.2f}")
            
            if account_purchase.index(order) != len(account_purchase) - 1:
                print("\n" + "-" * 30)
                
        print("\n" + "=" * 30, "\n")
        
    system("pause")
    
    

def editAccount(un):
    account_index = [acc[0] for acc in account_storage].index(un)
    account_details = account_storage[account_index]
    storeSign()
    
    print("        ACCOUNT CENTER\n")
    print("=" * 30, "\n")
    print(f" Username: {account_details[0]}\n")
    print(f" Address: {account_details[2]}")
    print(f" Contact #: {account_details[3]}\n")
    print(f" Password: {account_details[1]}\n")
    print("=" * 30, "\n")
    print(" [A] - EDIT ADDRESS")
    print(" [N] - EDIT CONTACT #")
    print(" [P] - EDIT PASSWORD")
    print(" [M] - RETURN TO MAIN MENU\n")
    print("=" * 30 + "\n\n")
    
    while True:
        choice = input("\033[1A\033[K Choice: ")

        if choice.upper() in "ANPM" and len(choice) == 1:
            break
        else:
            errorMessage()
            
    storeSign()
    
    print("        ACCOUNT CENTER\n")
    print("=" * 30, "\n")
    print(f" Username: {account_details[0]}\n")
    print(f" Address: {account_details[2]}")
    print(f" Contact #: {account_details[3]}\n")
    print(f" Password: {account_details[1]}\n")
    print("=" * 30, "\n")
    
    if choice in "aA":
        print(" - Addresses must not contain\n   spaces or punctuation")
        print(" - Addresses must be at least\n  3 characters in length")
        print(" - Replace spaces with a dash\n   for addresses\n")
        print("=" * 30, "\n")
        print(' *Type "-1" at the prompt\n  to return to main menu*\n')
        print("=" * 30, "\n\n")
        
        new_detail = AddressInput()
        
        if new_detail == None:
            return None
        
        edited_account = (account_details[0], account_details[1], new_detail, account_details[3])
    elif choice in "nN":
        print(" - Contact numbers must be 11\n   digits in length\n")
        print("=" * 30, "\n")
        print(' *Type "-1" at the prompt\n  to return to main menu*\n')
        print("=" * 30, "\n\n")
        
        new_detail = ContactNoInput(account_storage)
        
        if new_detail == None:
            return None
        
        edited_account = (account_details[0], account_details[1], account_details[2], new_detail)
    elif choice in "pP":
        print(" - Passwords must be at least\n   8 characters in length")
        print(" - Passwords must contain at\n   least 1 uppercase letter")
        print(" - Passwords must contain at\n   least 1 number")
        print(" - New password must not be \n   similar to previous password\n")
        print("=" * 30, "\n")
        print(' *Type "-1" at the prompt\n  to return to main menu*\n')
        print("=" * 30, "\n\n")
        
        new_detail = PasswordInput(account_details[1])
        
        if new_detail == None:
            return None
        
        edited_account = (account_details[0], new_detail, account_details[2], account_details[3])
    elif choice in "mM":
        return None
    
    storeSign()
    
    print("        ACCOUNT CENTER\n")
    print("=" * 30, "\n")
    print("       ORIGINAL DETAILS")
    print(f" Username: {account_details[0]}\n")
    print(f" Address: {account_details[2]}")
    print(f" Contact #: {account_details[3]}\n")
    print(f" Password: {account_details[1]}\n")
    print("=" * 30, "\n")
    print("        EDITED PRODUCT")
    print(f" Username: {edited_account[0]}\n")
    print(f" Address: {edited_account[2]}")
    print(f" Contact #: {edited_account[3]}\n")
    print(f" Password: {edited_account[1]}\n")
    print("=" * 30, "\n\n")
    
    while True:
        confirm_prompt = input("\033[1A\033[K Confirm Edit [Y/N]: ")

        if confirm_prompt.upper() in "YN" and len(confirm_prompt) == 1:
            break
        else:
            errorMessage()
    
    if confirm_prompt in "nN":
        return None
    
    account_storage[account_index] = edited_account
    
    storeSign()
    print("        ACCOUNT CENTER\n")
    print("=" * 30, "\n")
    print(" SUCCESSFULLY EDITED ACCOUNT\n")
    print("=" * 30, "\n\n")
    
    system("cls")


def orderInput():
    product_no_input = productNumber(product_list)
    
    if product_no_input == None:
        return None
    
    order_quantity_input = orderQuantity(product_no_input, product_list)
    
    if order_quantity_input == None:
        return None
    
    new_order_input = (product_no_input, order_quantity_input)
    
    return new_order_input
    


def paymentInput(order_list):
    order_details = order_list
    
    prod_details = product_list[order_details[0] - 1]
    
    payment_total = prod_details[1] * order_list[1]
    
    storeSign()
    print("       PAYMENT SECTION\n")
    print("=" * 30, "\n")
    print("        Order Details")
    print(f" Product Name: {prod_details[0]}")
    print(f" Price: PHP {prod_details[1]:.2f}\n")
    print(f" Quantity: {order_list[1]}\n")
    print(f" Payment Total: PHP {payment_total:.2f}\n")
    print("=" * 30, "\n")
    print(' *Type "-1" at the payment \n  amount prompt to return to\n  cancel purchase*\n')
    print("=" * 30, "\n\n")
    
    payment_amount = paymentAmount(payment_total)
    
    change_amount = payment_amount - payment_total
    
    payment_details = (payment_amount, change_amount)

    return payment_details



def receipt(username, order_list, payment_info):
    un = username
    
    prod_no = order_list[0]
    
    prod_details = product_list[prod_no - 1]
    prod_name = prod_details[0]
    prod_price = prod_details[1]
    
    ord_quantity = order_list[1]
    
    payment_total = prod_price * ord_quantity
    
    amount_paid = payment_info[0]
    change_received = payment_info[1]
    
    purchase = (un, prod_no, prod_name, ord_quantity, payment_total, amount_paid, change_received)
    
    return purchase



def editStock(receipt):
    purchase_info = receipt
    
    prod_no = purchase_info[1]
    ord_quantity = purchase_info[3]
    
    prod_to_edit = product_list[prod_no - 1]
    
    old_stock = prod_to_edit[2]
    
    new_stock = old_stock - ord_quantity
    
    new_info = (prod_to_edit[0], prod_to_edit[1], new_stock)
    
    return new_info