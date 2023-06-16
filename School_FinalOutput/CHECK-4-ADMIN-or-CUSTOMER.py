import os
import time

class Tindahan:
    rjp_product = {}
    pcode = 1
        
    def display_rjp_product(self):
        print("\nApollo Tindahan")
        for each_p in self.rjp_product.keys():
            pro_details = self.rjp_product[each_p]
            print(f"{each_p} - {pro_details[0]} @ Php {pro_details[1]}")

    def add_product(self, pname, pprice, pstock):
        self.product_name = pname
        self.product_price = pprice
        self.product_stock = pstock

        self.rjp_product[self.pcode] = (self.product_name, self.product_price, self.product_stock)
        Tindahan.pcode += 1
        tindahan.save_products()

    def edit_product(self, pcode, pname, pprice, pstock):
        if pcode in self.rjp_product:
            self.rjp_product[pcode] = (pname, pprice, pstock)
            print(f"Product with code {pcode} has been updated.")
            self.save_products()  # Save the product list
        else:
            print("Invalid product code.")

    def delete_product(self, pcode): # this functions deletes products
        if pcode in self.rjp_product:
            del self.rjp_product[pcode]
            print(f"Product with code {pcode} has been deleted.")
            self.reassign_product_codes()
            self.save_products()  # Save the product list
        else:
            print("Invalid product code.")

    def reassign_product_codes(self):
        new_rjp_product = {}
        new_pcode = 1
        for pcode in self.rjp_product.keys():
            new_rjp_product[new_pcode] = self.rjp_product[pcode]
            new_pcode += 1
        self.rjp_product = new_rjp_product
        Tindahan.pcode = new_pcode

    def save_products(self):
        with open("product_list.txt", "w") as file: 
            file.write("")
        with open("product_list.txt", "a") as file: 
            for pcode in self.rjp_product.keys():
                pname, pprice, pstock = self.rjp_product[pcode]
                file.write(f"{pname},{pprice},{pstock}\n")

    def load_products(self):
        try:
            with open("product_list.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        values = line.split(",")
                        if len(values) == 3:
                            pname, pprice, pstock = values
                            self.add_product(pname, float(pprice), int(pstock))
                        else:
                            print(f"Invalid line format: {line}")
        except FileNotFoundError:
            print("Product list file not found.")


class Customer:
    customer_records_file = "customer_records.txt"
    c_customer = {}

    def __init__(self, c_id, c_name, c_address):
        self.customer_id = c_id
        self.customer_name = c_name
        self.customer_address = c_address
        self.customer_record()

    def customer_record(self):
        self.c_customer[self.customer_id] = (self.customer_name, self.customer_address)
        Customer.save_customer_records()

    @staticmethod
    def save_customer_records():
        with open(Customer.customer_records_file, "w") as file:
            file.write("")
        with open(Customer.customer_records_file, "a") as file:
            for customer_id, details in Customer.c_customer.items():
                file.write(f"{customer_id},{details[0]},{details[1]}\n")

    @staticmethod
    def load_customer_records():
        try:
            with open(Customer.customer_records_file, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        values = line.split(",")
                        if len(values) == 3:
                            c_id, c_name, c_address = values
                            Customer.c_customer[int(c_id)] = (c_name, c_address)
                        else:
                            print(f"Invalid line format in customer records: {line}")
        except FileNotFoundError:
            print("Customer records file not found.")

    @staticmethod
    def display_customer_records():
        print("\nMga Suki")
        for customer_id, details in Customer.c_customer.items():
            print(f"{customer_id}-{details[0]} {details[1]}")


class Sales:
    def __init__(self, tindahan):
        self.display_rjp_product(tindahan)
        self.buy_my_product(tindahan)

    def display_rjp_product(self, tindahan):
        tindahan.display_rjp_product()

    def buy_my_product(self, tindahan):
        self.customer_choice = int(input("Enter your choice: "))
        self.customer_quantity = int(input("Enter number of quantity: "))

        self.customer_id = int(input("Enter Customer ID: "))

        if self.customer_id in Customer.c_customer:
            i_detail = tindahan.rjp_product[self.customer_choice]
            c_detail = Customer.c_customer[self.customer_id]
            product_name = i_detail[0]
            product_price = i_detail[1]
            total_amount = product_price * self.customer_quantity

            print(f"{c_detail[0]}, Please pay an amount of Php {total_amount} for {self.customer_quantity} {product_name}(s).")

            file_rico_inventory = open("rico_inventory.txt", "a")

            sales_rec = f"{self.customer_id} {c_detail[0]} {self.customer_choice} {i_detail[0]} {self.customer_quantity} {self.customer_quantity * i_detail[1]}\n"

            file_rico_inventory.write(sales_rec)
            file_rico_inventory.close()
        else:
            print("Invalid customer ID.")


class Inventory:
    def __init__(self, tindahan):
        self.display_inventory(tindahan)

    def display_inventory(self, tindahan):
        inventory_file = "rico_inventory.txt"
        if os.path.exists(inventory_file):
            try:
                with open(inventory_file, "r") as file_rico_inventory:
                    sales_rec = file_rico_inventory.readline()
                    sales_amt = 0
                    rico_item = {}

                    while sales_rec != '':
                        sales_details = sales_rec.split()
                        sales_amt += int(sales_details[4])

                        if int(sales_details[2]) in rico_item:
                            rico_item[int(sales_details[2])] += int(sales_details[4])
                        else:
                            rico_item[int(sales_details[2])] = int(sales_details[4])
                        
                        print(sales_details) # Edit this to display what you want
                        sales_rec = file_rico_inventory.readline()

                    for item in tindahan.rjp_product:
                        sales_qty = rico_item.get(item, 0)

                        item_detail = tindahan.rjp_product[item]
                        new_item_detail = (item_detail[0], item_detail[1], item_detail[2] - sales_qty)
                        tindahan.rjp_product[item] = new_item_detail

                    
            except FileNotFoundError:
                print("Error: Failed to read the inventory file.")
        else:
            print("Error: Inventory file not found.")


def admin_login():
    print("\nAdmin Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "password":
        return True
    else:
        print("Invalid username or password.")
        return False


def customer_login(customer1):
    print("\nCustomer Login")
    while True:
        customer_id = int(input("Enter your customer ID: "))
        clear_screen()
        if customer_id in customer1.c_customer:
            customer_name = customer1.c_customer[customer_id][0]
            print(f"Welcome, {customer_name}!")
            return customer_id

        print("Invalid customer ID. Please try again.")


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def menu():
    
    admin_logged_in = False
    customer_logged_in = False
    
    while not (admin_logged_in or customer_logged_in):
        print("\nWelcome to Apollo Tindahan!")
        print("Choose an option:")
        print("[1] Admin Login")
        print("[2] Customer Login")
        login_option = input("Enter your choice: ")

        if login_option == '1':
            clear_screen()
            admin_logged_in = admin_login()
            clear_screen()
            if not admin_logged_in:
                clear_screen()
        elif login_option == '2':
            clear_screen()
            customer_id = customer_login(customer1)
            if customer_id is not None:
                customer_logged_in = True
            else:
                clear_screen()
        else:
            clear_screen()
            print("Invalid choice.")
    
    if admin_logged_in:
        admin_menu()
    elif customer_logged_in:
        customer_menu()

def admin_menu():
    rpt = "Y"
    while rpt == "Y":
        print("\nApollo Tindahan - Admin Menu")
        print("[1] Add a Product")
        print("[2] Edit a Product")
        print("[3] Delete a Product")
        print("[4] View Products") 
        print("[5] Add a Customers")
        print("[6] View Customer")
        print("[7] Generate Inventory Report")
        print("[8] Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            clear_screen()
            pname = input("Enter the product name: ")
            pprice = float(input("Enter the product price: "))
            pstock = int(input("Enter the product stock: "))
            tindahan.add_product(pname, pprice, pstock)
            print(tindahan.rjp_product)
            print("Product added successfully.")
            time.sleep(3)
            clear_screen()
        elif choice == '2':
            clear_screen()
            tindahan.display_rjp_product()
            pcode = int(input("Enter the product code you want to edit: "))
            if pcode in tindahan.rjp_product:
                pname = input("Enter the new product name: ")
                pprice = float(input("Enter the new product price: "))
                pstock = int(input("Enter the new product stock: "))
                tindahan.edit_product(pcode, pname, pprice, pstock)
                print("Product edited successfully.")
            else:
                print("Invalid product code.")
            time.sleep(3)
            clear_screen()
        elif choice == '3':
            clear_screen()
            tindahan.display_rjp_product()
            pcode = int(input("Enter the product code you want to delete: "))
            tindahan.delete_product(pcode)
            print("Product deleted successfully.")
            time.sleep(3)
            clear_screen()
        elif choice == '4':
            clear_screen()
            tindahan.display_rjp_product()
            time.sleep(3)
            clear_screen()
        elif choice == '5':
            clear_screen()
            c_id = int(input("Enter the customer ID: "))
            c_name = input("Enter the customer name: ")
            c_address = input("Enter the customer address: ")
            customer = Customer(c_id, c_name, c_address)
            print("Customer added successfully.")
            time.sleep(10)
            clear_screen()
        elif choice == '6':
            clear_screen()
            Customer.display_customer_records()
            time.sleep(3)
            clear_screen()
        elif choice == '7':
            clear_screen()
            inventory_store = Inventory(tindahan)
            time.sleep(10)
            clear_screen()
        elif choice == '8':
            clear_screen()
            print("Thank you for visiting Apollo Tindahan!")
            break
        else:
            clear_screen()
            print("Invalid Choice!")

        rpt = input("Do you want to return to the main menu? (Y/N): ").upper()
        clear_screen()
        if rpt == "N":
            print("Thank you for shopping at Apollo Tindahan!")
            
def customer_menu():
    rpt = "Y"
    while rpt == "Y":
        print("\nApollo Tindahan - Customer Menu")
        print("[1] Buy a Product")
        print("[2] View Products")
        print("[3] Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            clear_screen()
            sales = Sales(tindahan)
            time.sleep(3)
            clear_screen()
            choice = input("Do you want to buy again? (Y/N): ").upper()
            clear_screen()
            if choice == "N":
                print("Thank you for shopping at Apollo Tindahan!")
                break
        elif choice == '2':
            clear_screen()
            tindahan.display_rjp_product()
            time.sleep(3)
            clear_screen()
        elif choice == '3':
            clear_screen()
            print("Thank you for shopping at Apollo Tindahan!")
            break
        else:
            clear_screen()
            print("Invalid Choice!")

        rpt = input("Do you want to return to the main menu? (Y/N): ").upper()
        clear_screen()
        if rpt == "N":
            print("Thank you for shopping at Apollo Tindahan!")

tindahan = Tindahan()
tindahan.load_products()
menu()



    