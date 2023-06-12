from rich import print
from rich.console import Console
from rich.table import Table
from time import sleep



console = Console(width=100)



# ========== Main Store | Where All the products are placed ==========
class Shun_Store:
    Shun_items = {}
    pcode = 1

    def __init__(self, pname, pprice, pstock):
        self.product_name = pname
        self.product_price = pprice
        self.product_stock = pstock

        self.Shun_items[self.pcode] = (self.product_name, self.product_price, self.product_stock)
        self.pcode += 1

    def display_Shun_product():
        print("Shun's Store")
        for each_p in Shun_Store.Shun_items.keys():
            pro_details = Shun_Store.Shun_items[each_p]
            print(f"{str(each_p)} - {str(pro_details[0])} @ Php {str(pro_details[1])}\n")
        

    
c_customer = {}

# ========== Customer =========
class Customer:
    '''This handles customer data'''

    def __init__(self, cid, cname, caddress, cust_dic):
        self.customer_id = cid
        self.customer_name = cname
        self.customer_address = caddress
        self.cust_dic = cust_dic
        self.add_to_record(self.cust_dic)

    # this function adds the customers to the record
    def add_to_record(self, c_customer):
        c_customer[self.customer_id] = (self.customer_name, self.customer_address)


    def customer_record(self):
        table = Table()
        console.print("\n🔎 View Customer \n", style="bold white on cyan", justify="center")
        
        # Table
        table.add_column("Customer ID", style="cyan", no_wrap=True)
        table.add_column("Customer Name", style="green")
        table.add_column("Customer Adress", justify="right", style="red")

        for key, value in self.cust_dic.items():
            table.add_row(str(key), value[0], value[1])
        
        print(table)





# ========== Sales =========
class Sales:
    '''This handles customer transactions with the store'''
    def __init__(self):
        self.display_Shuns_product()
        self.buy()  


    # ========= Display the products in the store
    def display_Shuns_product(self):
        print("My store")
        for each_prod in S_Summer_shirt.Shun_items.keys():
            pro_details = S_Summer_shirt.Shun_items[each_prod]
            print(f"[{str(each_prod)}] - {str(pro_details[0])} @ Php {str(pro_details[1])}")

    def buy(self):
        self.customer_choice = int(input("Enter the number of your choice: "))
        self.customer_quantity = int(input("Enter number quantity: "))
        self.customer_id = int(input("Enter customer ID: "))

        item_detail = S_Summer_shirt.Shun_items[self.customer_choice]
        c_detail = first_customer.c_customer[self.customer_id]

        print(c_detail[0] + ", Please pay an amount of", self.customer_quantity * item_detail[1], "pesos only")
        
        with open("Shun_inventory.txt", "a") as file_Shun_inventory:
                               
            sales_record = str(self.customer_id) + " " + str(item_detail[0]) + " "
            sales_record += str(self.customer_choice) + " " + str(item_detail[0]) + " " + str(self.customer_quantity) + " "
            sales_record += str(self.customer_quantity * item_detail[1]) + "\n"

            file_Shun_inventory.write(sales_record)                                         






# ========== K Inventory ==========
class Sudars_inventory():
    '''This stores the sales details in a text file'''
    def __init__(self):
        self.display_inventory()


    def display_inventory(self):
        with open("Shun_inventory.txt", "r") as file_S_inventory:
            sales_record = file_S_inventory.readline()
            sales_amount = 0
            Shuns_item = {}

            while sales_record != '':
                print(sales_record, end='')

                sales_details = sales_rec.split()
                sales_amount += int(sales_details[5])

                if int(sales_details[2]) in Shuns_item:
                    Shuns_item[int(sales_details[2])] += (sales_details[4],)
                else:
                    Shuns_item[int(sales_details[2])] = (sales_details[4],)
                    
                sales_rec = file_S_inventory.readline()

S_Summer_shirt = Shun_Store("shirt_one", 100, 20) 
S_Summer_short = Shun_Store("Pants_one", 150, 15)


first_customer = Customer(14, "Shawn", "Cebu City, Cebu", c_customer)
second_customer = Customer(16, "Eloisa", "Pinabacdao, Samar", c_customer)
third_customer = Customer(67, "Krizzel", "Albuera, Leyte", c_customer)




# ========== First funtion to be called ==========
def menu():

    rpt = "Y"

    while rpt == "Y":
        console.print("\n🩳 たかい's Online Store 👕\n", style="bold white on cyan", justify="center")
        console.print("""\nSystem Menu
        [1] Buy a product
        [2] View Products
        [3] View Customers
        [4] Generate Inventory Report
        [5] Exit""")

        
        c = int(input("Enter your Choice: "))

        if c == 1: #For buying items
            s_rec = Sales()

        elif c == 2: # for displaying all the products
            Shun_Store.display_Shun_product()

        elif c == 3: # Get specified customer record
            first_customer.customer_record()

        elif c == 4: #
            Sudars_inven = Sudars_inventory()

        elif c == 5:
            print("Thank You! Come Again.")
            rpt = "N"
        else:
            print("Enter the right number of choices!")
menu()
