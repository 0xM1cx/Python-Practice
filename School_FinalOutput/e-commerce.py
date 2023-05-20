class DG_Product:
    dgProduct = {}
    pcode = 1

    def __init__(self, pname, pprice, pstock):
        self.productName = pname
        self.productPrice = pprice
        DG_Product.productStock = pstock

        self.dgProduct[self.pcode] = (self.productName, self.productPrice, self.productStock)
        DG_Product.pcode += 1

    def display_DG_Product(self):
        print("DG Store")
        for each_p in self.dgProduct.keys():
            pro_Details = self.dgProduct[each_p]
            print(str(eac_p) + ' - ' + str(pro_Details[0]) + ' @ Php' + str(pro_Details[1]))
        return ''

# handles sales
class Sales:
    def __init__(self):
        self.display_DG_Product()
        self.selling()

    
    def display_DG_Product(self):
        print("DG Store")
        for each_p in self.dgProduct.keys():
            pro_Details = self.dgProduct[each_p]
            print(str(each_p) + ' - ' + str(pro_Details[0]) + ' @ Php' + str(pro_Details[1]))
        return ''

    def selling(self):
        self.customerChoice = int(input("Enter the number of your choice: "))
        self.customerQuantity = int(input("Enter the quantity: "))
    
        self.customerId = int(input("enter Customer ID: "))

        iDetail = dg_shirt.dg_product(self.customerChoice())
        cDetail - cr.1.c_cutomer

guest = []

def customers():
    cusGuest = input("Customers name: ")
    guest.append(cusGuest)

def add_Product():
    pass

def menu():
    rpt = 'Y'
    while rpt == 'Y':
        print("\nDG Online Store")
        print('''\nSystem Menu
        [1] Buy a Product
        [2] View Product
        [3] View Customers
        [4] Generate Inverntory Report
        [5] Exit
        ''')
        ch = input("Enter your Choice: ")
        print('\n')

        if ch == '1':
            print("Buy a Product")
            customers()
            
        elif ch == '2':
            customers()
            dg_tshirt.display_DG_Product()
        elif ch == '3':
            print("Recent ustomers")
            for cus in guest:
                print(cus)
        elif ch == '4':
            print("Generate Inventory Report")
        elif ch == '5':
            print('Thank You!')
            rpt = 'N'
        else:
            print("Invalid input")


class Customer:
    c_customer = {}
    
    def __init__(self, cid, cname, caddress):
        self.customer_id = cid
        self.customer_name = cname
        self.customer_address = caddress

class DG_inventory():
    def __init__(self):
        self.display_inventory()
    
    def display_inventory(self):
        file_dg_inventory = open("dg_inventory.txt", "t")
        sales_rec = file_dg_inventory.readline()
        sales_amt = 0
        dg_item = []

        while sales_rec != '':
            print(sales_rec, end='')

dg_tshirt = DG_Product('Mark', 150, 20)
dg_pants = DG_Product('Martin', 200, 25)
menu()
