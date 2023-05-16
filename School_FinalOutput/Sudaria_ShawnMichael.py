from colorama import Fore


# ========== Main Store ==========
class K_Store:
    k_store = {}
    pcode = 1

    def __init__(self, pname, pprice, pstock):
        self.product_name = pname
        self.product_price = pprice
        K_Store.product_stock = pstock

        self.k_store[self.pcode] = (self.product_name, self.product_price, self.product_stock)
        K_Store.pcode += 1

    def display_K_product(self):
        print("K's Store")
        for each_p in self.k_store.keys():
            pro_details = self.k_store[each_p]
            print(f"{str(each_p)} - {str(pro_details[0])} @ Php {str(pro_details[1])}")
        return ''



# ========== Customer =========
class Customer:
    '''This handles customer data'''
    c_customer = {}

    def __init__(self, cid, cname, caddress):
        self.customer_id = cid
        self.customer_name = cname
        self.customer_address = caddress
        self.customer_record()

    def customer_record(self):
        print("View Customers")
        self.c_customer[self.customer_id] = (self.customer_name, self.customer_address)
        return self.c_customer[self.customer_id]


# ========== Sales =========
class Sales:
    '''This handles customer transactions with the store'''
    def __init__(self):
        self.display_K_product()
        self.buy()

    def display_K_product(self):
        print("My store")
        for each_p in S_shirt.k_store.keys():
            pro_details = S_shirt.k_store[each_p]
            print(f"[{str(each_p)}] - {str(pro_details[0])} @ Php {str(pro_details[1])}")

    def buy(self):
        self.customer_choice = int(input("Enter the number of your choice: "))
        self.customer_quantity = int(input("Enter number quantity: "))
        self.customer_id = int(input("Enter customer ID: "))

        item_detail = S_shirt.k_store[self.customer_choice]
        c_detail = first_customer.c_customer[self.customer_id]

        print(c_detail[0] + ", Please pay an amount of", self.customer_quantity * item_detail[1], "pesos only")
        
        file_k_inventory = open("k_inventory.txt", "a")
                               
        sales_rec = str(self.customer_id) + " " + str(item_detail[0]) + " "
        sales_rec += str(self.customer_choice) + " " + str(item_detail[0]) + " " + str(self.customer_quantity) + " "
        sales_rec += str(self.customer_quantity * item_detail[1]) + "\n"

        file_k_inventory.write(sales_rec)
        file_k_inventory.close()                                                



# ========== K Inventory ==========
class Sudars_inventory():
    '''This stores the sales details in a text file'''
    def __init__(self):
        self.display_inventory()

    def display_inventory(self):
        file_S_inventory = open("k_inventory.txt", "r")
        sales_rec = file_S_inventory.readline()
        sales_amt = 0
        k_item = {}

        while sales_rec != '':
            print(sales_rec, end='')

            sales_details = sales_rec.split()
            sales_amt += int(sales_details[5])

            if int(sales_details[2]) in k_item:
                k_item[int(sales_details[2])] += (sales_details[4],)
            else:
                k_item[int(sales_details[2])] = (sales_details[4],)
                
            sales_rec = file_S_inventory.readline()

def menu():

    rpt = "Y"
    while rpt == "Y":
        print(Fore.BLUE, "\nSudaria's Online Store")
        print(Fore.GREEN, """\nSystem Menu
        [1] Buy a product
        [2] View Products
        [3] View Customers
        [4] Generate Inventory Report
        [5] Exit""")
        c = int(input("Enter your Choice: "))

        if c == 1:
            s_rec = Sales()

        elif c == 2:
            S_shirt.display_K_product()

        elif c == 3:
            print(first_customer.customer_record())

        elif c == 4:
            k_os = Sudars_inventory()

        elif c == 5:
            print("Thank You! Come Again.")
            rpt = "N"
        else:
            print("Enter the right number of choices!")

S_shirt = K_Store("shirt", 100, 20)
S_pants = K_Store("Pants", 150, 15)

first_customer = Customer(12, "Shawn", "Tacloban City, Leyte")

menu()
