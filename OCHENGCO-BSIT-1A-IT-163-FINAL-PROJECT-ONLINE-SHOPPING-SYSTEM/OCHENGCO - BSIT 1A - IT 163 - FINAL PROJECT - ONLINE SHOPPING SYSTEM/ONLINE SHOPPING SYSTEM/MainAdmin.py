from os import system
from time import sleep
import AccountCenter as AC
from InputAdmin import prodName, prodPrice, prodStock, amountSold, readProductStorage, writeProductStorage
from InputCustomer import readInventoryReport
from ScreensStore import storeSignAdmin, mainScreenAdmin, productCenterScreen, editProductScreen, inventoryCenterScreen, productCreationGuidelines, logOutScreen, errorMessage



product_list = []
purchase_list = []



class Store():
    def __init__(self, prod_name, prod_price, prod_stock):
        self.prod_name = prod_name
        self.prod_price = prod_price
        self.prod_stock = prod_stock
        
    def addProduct(self):
        storeSignAdmin()
        print("       ADDING PRODUCTS\n")
        print("=" * 30, "\n")
        productCreationGuidelines()
        print(' *Type -1 at the prompt to\n  cancel the process*\n')
        print("=" * 30, "\n\n")
            
        new_product = productInput()
        
        if new_product == None:
            return None
        
        storeSignAdmin()
        print("       ADDING PRODUCTS\n")
        print("=" * 30, "\n")
        print("   PRODUCT ADDITON OVERVIEW")
        print(f"Product Name: {new_product[0]}")
        print(f"Product Price: PHP {new_product[1]:.2f}")
        print(f"Amount in Stock: {new_product[2]}\n")
        print("=" * 30, "\n\n")
        
        while True:
            confirm_prompt = input("\033[1A\033[K Confirm Addition [Y/N]: ")

            if confirm_prompt.upper() in "YN" and len(confirm_prompt) == 1:
                break
            else:
                errorMessage()
        
        if confirm_prompt in "nN":
            return None
        
        product_list.append(new_product)
        
        storeSignAdmin()
        print(" SUCCESSFULLY ADDED PRODUCTS\n")
        print("=" * 30, "\n\n")
        
        while True:
            view_prompt = input("\033[1A\033[K View Product Database? [Y/N]: ")
            
            if view_prompt.upper() in "YN" and len(view_prompt) == 1:
                break
            else:
                errorMessage()
                
        if view_prompt in "Yy":
            admin.viewProduct()
            system("pause")
         
    def editProduct(self):
        self.viewProduct()
        
        if len(product_list) != 0:
            print("       EDITING PRODUCT\n")
            print("=" * 30, "\n")
            print(' *Type -1 at the prompt to\n  cancel the process*\n')
            print("=" * 30, "\n\n")
            
            while True:
                try:
                    prod_id = int(input("\033[1A\033[K Enter product #: "))

                    if prod_id == -1:
                        return None
                    elif prod_id <= 0:
                        errorMessage()
                    elif prod_id > len(product_list):
                        sleep(0.5)
                        print("\033[1A\033[K    PRODUCT DOES NOT EXIST")
                        sleep(1.25)
                    else:
                        break
                except:
                    errorMessage()
            
            editProductScreen()
            print("       PRODUCT TO EDIT")
            print(f"Product Name: {product_list[prod_id - 1][0]}")
            print(f"Product Price: PHP {product_list[prod_id - 1][1]:.2f}")
            print(f"Amount in Stock: {product_list[prod_id - 1][2]}\n")
            print("=" * 30, "\n")
            print(" [P] - CHANGE PRODUCT PRICE")
            print(" [S] - ADD TO PRODUCT STOCK")
            print(" [X] - RETURN TO PRODUCT CENTER\n")
            print("=" * 30, "\n\n")
            
            while True:
                choice = input("\033[1A\033[K Choice: ")

                if choice.upper() in "PSX" and len(choice) == 1:
                    break
                else:
                    errorMessage()
                    
            editProductScreen()
            print("       PRODUCT TO EDIT")
            print(f"Product Name: {product_list[prod_id - 1][0]}")
            print(f"Product Price: PHP {product_list[prod_id - 1][1]:.2f}")
            print(f"Amount in Stock: {product_list[prod_id - 1][2]}\n")
            print("=" * 30, "\n")
            print(' *Type -1 at the prompt to\n  cancel the process*\n')
            print("=" * 30, "\n")
                    
            if choice in "pP":
                new_detail = prodPrice()
                
                if new_detail == None:
                    return None
                
                edited_product = (product_list[prod_id - 1][0], new_detail, product_list[prod_id - 1][2])
            elif choice in "sS":
                new_detail = prodStock()
                
                if new_detail == None:
                    return None
                
                edited_product = (product_list[prod_id - 1][0], product_list[prod_id - 1][1], product_list[prod_id - 1][2] + new_detail)
            elif choice in "xX":
                return None
            
            editProductScreen()
            print("       ORIGINAL PRODUCT")
            print(f"Product Name: {product_list[prod_id - 1][0]}")
            print(f"Product Price: PHP {product_list[prod_id - 1][1]:.2f}")
            print(f"Amount in Stock: {product_list[prod_id - 1][2]}")
            print("\n" + "-" * 30)
            print("\n        EDITED PRODUCT")
            print(f"Product Name: {edited_product[0]}")
            print(f"Product Price: PHP {edited_product[1]:.2f}")
            print(f"Amount in Stock: {edited_product[2]}\n")
            print("=" * 30, "\n\n")
            
            while True:
                confirm_prompt = input("\033[1A\033[K Confirm Edit [Y/N]: ")

                if confirm_prompt.upper() in "YN" and len(confirm_prompt) == 1:
                    break
                else:
                    errorMessage()
            
            if confirm_prompt in "nN":
                return None
            
            product_list[prod_id - 1] = edited_product
            
            storeSignAdmin()
            print(" SUCCESSFULLY EDITED PRODUCT\n")
            print("=" * 30, "\n\n")
            
            while True:
                view_prompt = input("\033[1A\033[K View Product Database? [Y/N]: ")
                
                if view_prompt.upper() in "YN" and len(view_prompt) == 1:
                    break
                else:
                    errorMessage()
                    
            if view_prompt in "Yy":
                admin.viewProduct()
                system("pause")
        
        else:
            system("pause")
                
    def viewProduct(self):
        storeSignAdmin()
        print("       PRODUCT DATABASE\n")
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
    
    

admin = Store(None, None, None)



def adminMode():
    global product_list
    global purchase_list
    
    product_list = []
    product_list = readProductStorage(product_list)
        
    purchase_list = []
    purchase_list = readInventoryReport(purchase_list)
    
    mainScreenAdmin()
    
    while True:
        choice = input("\033[1A\033[K Choice: ")

        if choice.upper() in "PCIX" and len(choice) == 1:
            break
        else:
            errorMessage()
            
    if choice in "pP":
        productCenter()
    elif choice in "cC":
        AC.customerList()
    elif choice in "iI":
        inventoryCenter()
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
            
    adminMode()
    
    

def productCenter():
    productCenterScreen()
    
    while True:
        choice = input("\033[1A\033[K Choice: ")

        if choice.upper() in "AEVM" and len(choice) == 1:
            break
        else:
            errorMessage()
            
    if choice in "aA":
        admin.addProduct()
        writeProductStorage(product_list)
    elif choice in "eE":
        admin.editProduct()
        writeProductStorage(product_list)
    elif choice in "vV":
        admin.viewProduct()
        system("pause")
    elif choice in "mM":
        return None
    
    productCenter()



def inventoryCenter():
    inventoryCenterScreen()
    
    while True:
        choice = input("\033[1A\033[K Choice: ")

        if choice.upper() in "IPM" and len(choice) == 1:
            break
        else:
            errorMessage()
            
    if choice in "iI":
        viewInventory()
    elif choice in "pP":
        purchaseHistory()
    elif choice in "mM":
        return None
    
    inventoryCenter()



def viewInventory():
    storeSignAdmin()
    print("       PRODUCT DATABASE\n")
    print("=" * 30)
    
    if len(product_list) == 0:
        print("\n        WOW SUCH EMPTY\n")
        print("=" * 30, "\n")
    elif len(product_list) != 0:
        for prod in product_list:
            amount_sold = amountSold(product_list.index(prod), purchase_list)
            
            print(f"\n          PRODUCT # {product_list.index(prod) + 1}")
            
            print(f"Product Name: {prod[0]}")
            print(f"Original Stock: {amount_sold + prod[2]}")
            print(f"Amount Sold: {amount_sold}")
            print(f"Current Stock: {prod[2]}")
            
            if product_list.index(prod) != len(product_list) - 1:
                print("\n" + "-" * 30)
                
        print("\n" + "=" * 30, "\n")
        
    system("pause")



def purchaseHistory():
    storeSignAdmin()
    print("       PURCHASE HISTORY\n")
    print("=" * 30)
    
    if len(purchase_list) == 0:
        print("\n        WOW SUCH EMPTY\n")
        print("=" * 30, "\n")
    elif len(product_list) != 0:
        for order in purchase_list:
            print(f"\n          PURCHASE # {purchase_list.index(order) + 1}")
            
            print(f" USERNAME: {order[0]}\n")
            print(f" PRODUCT NAME: {order[2]}")
            print(f" PRODUCT PRICE: PHP {order[4] / order[3]:.2f}\n")
            print(f" QUANTITY: {order[3]}\n")
            print(f" ORDER TOTAL: PHP {order[4]:.2f}\n")
            print(f" AMOUNT PAID: PHP {order[5]:.2f}")
            print(f" CHANGE RECEIVED: PHP {order[6]:.2f}")
            
            if purchase_list.index(order) != len(purchase_list) - 1:
                print("\n" + "-" * 30)
                
        print("\n" + "=" * 30, "\n")
        
    system("pause")



def productInput():
    prod_name_input = prodName(product_list)
    
    if prod_name_input == None:
            return None
        
    prod_price_input = prodPrice()
    
    if prod_price_input == None:
            return None
        
    prod_stock_input = prodStock()
    
    if prod_stock_input == None:
            return None
    
    new_product_input = Store(prod_name_input, prod_price_input, prod_stock_input)
    
    new_record_input = (new_product_input.prod_name, new_product_input.prod_price, new_product_input.prod_stock)
    
    return new_record_input