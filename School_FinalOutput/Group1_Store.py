from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep
import os

console = Console(width=100)

# THINGS TO ADD
# + Delete a Product
# + Edit Product
# + Edit Customer Info
# + Delete Customer



def loadingScreen(text):
    for _ in track(range(10), description=f"[green]{text}"):
                    sleep(0.2)

def Clearscreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# ========== Main Store | Where All the products are placed ==========
class S_Store:
    S_items = {}
    pcode = 1
    original_stock = {}
    def __init__(self, pname, pprice, pstock):
        self.product_name = pname
        self.product_price = pprice
        S_Store.product_stock = pstock
        S_Store.S_items[S_Store.pcode] = [self.product_name, self.product_price, self.product_stock]
        S_Store.pcode += 1 

    def display_Shun_product(self):
        prod_table = Table()
        console.print("\n🥼 たかい's Store Items 👔\n", style="bold white on cyan", justify="center")
        
        # Product Table
        prod_table.add_column("Product ID", style="cyan", no_wrap=True, justify="center")
        prod_table.add_column("Product Name", style="green", justify="center")
        prod_table.add_column("Product Price", style="blue", justify="center")
        prod_table.add_column("No.Product In-Stock", justify="center", style="red")

        for key, value in S_Store.S_items.items():
            prod_table.add_row(str(key), str(value[0]), f"₱ {str(value[1])}", str(value[2]))

        console.print(prod_table)

    def editProduct(prod_id, prod_name=None, prod_price=None, prod_stock=None):
        if prod_name != None:
            S_Store.S_items[prod_id][0] = prod_name
        
        if prod_price != None:
            S_Store.S_items[prod_id][1] = prod_price
        
        if prod_stock != None:
            S_Store.S_items[prod_id][2] = prod_stock


    
c_customer = {}
# ========== Customer =========
class Customer:
    '''This handles customer data'''

    def __init__(self, cid, cname, caddress):
        self.customer_id = cid
        self.customer_name = cname
        self.customer_address = caddress 
        c_customer[self.customer_id] = (self.customer_name, self.customer_address)


    def customer_record(self):
        table = Table()
        console.print("\n🔎 View Customer \n", style="bold white on cyan", justify="center")
        
        # Table
        table.add_column("Customer ID", style="cyan", no_wrap=True)
        table.add_column("Customer Name", style="green")
        table.add_column("Customer Adress", justify="right", style="red")


        for key, value in c_customer.items():
            table.add_row(str(key), value[0], value[1])
        
        print(table)



# ========== Sales =========
class Sales(S_Store):
    '''This handles customer transactions with the store'''
    def __init__(self):
        super().display_Shun_product() # Na inherit ha S_Store class an display function
        self.buy()  # gin call an buy function


    def buy(self):
        self.customer_choice = int(input("Enter the number of your choice: "))
        if int(super().S_items[self.customer_choice][2]) == 0:
            print("No more product in stock")
            print("Restarting...")
            sleep(2)
            self.buy()

        self.customer_quantity = int(input("Enter number quantity: "))
        self.customer_id = int(input("Enter customer ID: "))

        if self.customer_id not in c_customer: # Checking for user in database, if not, then allow to create new user
            print("Customer is not in database yet")
            uInput = input("Add customer? Y or N")
            if uInput == "Y" or "y":
                cust_ID = int(input("Customer ID: "))
                cust_Name = input("Customer Name: ")
                cust_Address = input("Customer Address: ")
                if " " in cust_Name:
                    cust_Name.replace(" ", "_")            
            
                new_cust = Customer(cust_ID, cust_Name, cust_Address)
                for _ in track(range(10), description="[green]Adding Customer To Database"):
                    sleep(0.2)
                Clearscreen()
            elif uInput == "N" or "n":
                self.buy()
            else:
                print("NOT VALID INPUT, please try again")
                sleep(2)
                self.buy()



        super().original_stock[self.customer_choice] = super().S_items[self.customer_choice][2]
        super().S_items[self.customer_choice][2] = int(super().S_items[self.customer_choice][2]) - self.customer_quantity
        item_detail = S_Store.S_items[self.customer_choice]
        c_detail = c_customer[self.customer_id]
        original_prod_Stock = super().original_stock[self.customer_choice]
        current_number_of_Stock = super().S_items[self.customer_choice][2]


        for _ in track(range(10), description="[green]Processing Sale"):
                sleep(0.2)

        print(c_detail[0] + ", Please pay an amount of", self.customer_quantity * item_detail[1], "pesos only")
        
        with open("S_inventory.txt", "a") as file_S_inventory:
                               
            sales_record = str(self.customer_id) + " " + str(item_detail[0]) + " "
            sales_record += str(self.customer_choice) + " " + str(item_detail[0]) + " " + str(self.customer_quantity) + " "
            sales_record += str(self.customer_quantity * item_detail[1]) + " "
            sales_record += str(original_prod_Stock) + " " + str(current_number_of_Stock) + "\n"
            file_S_inventory.write(sales_record)   
        sleep(2)
        Clearscreen()                                      




# ========== K Inventory ==========
class S_inventory(S_Store):
    '''This stores the sales details in a text file'''
    def __init__(self):
        self.display_inventory()


    def display_inventory(self):
        with open("S_inventory.txt", "r") as file_S_inventory:
            sales_record = file_S_inventory.readlines()
            sales_amount = 0
            S_item = {}
            cnt = 1

            for rec in sales_record:
                sales_details = rec.split()
                
                S_item[cnt] = [sales_details[0],sales_details[1], sales_details[6], sales_details[7], sales_details[4], sales_details[5]]
                cnt += 1
            
                inven_table = Table()
        
                # Product Table
                inven_table.add_column("Customer ID", style="cyan", no_wrap=True, justify="center") # value[0]
                inven_table.add_column("ITEM BOUGHT", style="green", justify="center") # value[1]
                inven_table.add_column("QUANTITY", style="blue", justify="center") # value [3]
                inven_table.add_column("ORIGINAL STOCK", justify="center", style="red") # value[3]
                inven_table.add_column("CURRENT STOCK", justify="center", style="red") # value[4]
                inven_table.add_column("TOTAL COST", justify="center", style="red") # value[3]
                
                
                for value in S_item.values():        
                    
                    inven_table.add_row(value[0], str(value[1]),  str(value[4]), str(value[2]), str(value[3]), str(value[5]))

            console.print(inven_table)

                
            sales_amount += int(sales_details[5])


            console.print(f"\nTotal Current Sales: {sales_amount}")



S_Summer_shirt = S_Store("Summer_Shirt_One", 100, 20) 
S_Summer_short = S_Store("Summer_Pants_One", 150, 15)
S_Winter_shirt = S_Store("Winter_Shirt_Two", 200, 20) 
S_Winter_short = S_Store("Winter_Pants_Two", 250, 15)


first_customer = Customer(14, "Shawn", "Cebu City, Cebu")
second_customer = Customer(16, "Eloisa", "Pinabacdao, Samar")
third_customer = Customer(67, "Krizzel", "Albuera, Leyte")
fourth_customer = Customer(37, "Jane", "Carigara,   Leyte")




# ========== First funtion to be called ==========
def menu():
    Clearscreen()
    rpt = "Y"
    
    while rpt == "Y":
        console.print("\n🩳 たかい's Online Store 👕\n", style="bold white on cyan", justify="center")  
        console.print("""\nSystem Menu
        [1] Buy a product
        [2] View Products
        [3] View Customers
        [4] Generate Inventory Report
        [5] Add A Product
        [6] Add A Customer
        [7] Edit A Product
        [8] Edit A Customer
        [9] Delete A Product
        [10] Delete A Customer
        [11] Exit""")

        
        c = int(input("Enter your Choice: "))

        if c == 1: #For buying items
            Clearscreen()
            s_rec = Sales()

        elif c == 2: # for displaying all the products
            Clearscreen()
            S_Store.display_Shun_product(None)

        elif c == 3: # Get specified customer record
            Clearscreen()
            first_customer.customer_record()
 
        elif c == 4: # View Inventory
            Clearscreen()
            S_inven = S_inventory()

        elif c == 5: # Add Product
            prod_name = input("Product Name: ")
            prod_price = int(input("Product Price: "))
            prod_stock = int(input("Product Stock: "))
            new_prod = S_Store(prod_name, prod_price, prod_stock)
            loadingScreen("Adding Product")
            Clearscreen()

        elif c == 6: # Add Customer
            cust_ID = int(input("Customer ID: "))
            cust_Name = input("Customer Name: ")
            cust_Address = input("Customer Address: ")
            if " " in cust_Name:
                cust_Name.replace(" ", "_")            
            
            new_cust = Customer(cust_ID, cust_Name, cust_Address)
            loadingScreen("Adding Customer to the Database")
            Clearscreen()
        elif c == 7: # Edit a Product
            try:
                prod_id = int(input("[Required] Product ID: "))
            except:
                print("Please Provide an ID")
                loadingScreen("Restarting")
                Clearscreen()
                menu()
    
            prod_name = input("Product Name: ")
            if " " in prod_name:
                prod_name.replace(" ", "_")
        
            prod_price = int(input("Product Price: "))
            
            prod_stock = int(input("Product Stock: "))
           
            edit = S_Store.editProduct(prod_id=prod_id, prod_name=prod_name, prod_price=prod_price, prod_stock=prod_stock)
        elif c == 11: # Exit
            Clearscreen()
            console.print("Thank You! Come Again.", style="bold white on cyan", justify="center")
            rpt = "N"
        else:
            print("Enter the right number of choices!")
            loadingScreen("Restarting")
            menu()
menu()
