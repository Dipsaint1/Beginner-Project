from Grocery_Database import Database
from Registration_Class import Registration
from Login_Class import Login, Password
from Shopping_Store import Shop
from Buyy import Buy
import sys
import time
import datetime


class Menu(Database, Registration, Password, Login, Shop, Buy):
    creation_date = datetime.date.today()

    """ Display a menu and respond to choices when run."""
    def display_menu(self):

        print("""
MENU
1. Signup
2. Login
3. Change your password
4. Edit stock(Administrator only)
5. Buy Items
0. Quit
""")

    def shopping_menu(self):
        print("""
        SHOPPING MENU
        1. show all products
        2. Add to stock inventory
        3. Add new product
        4. Change product price
        0. Quit
        """)
    """================================================================================"""
    def sign_up(self):
        time.sleep(1)
        print("WELCOME to cyber9ja.com")
        Registration.get_name(self)
        Registration.get_email(self)
        username = Registration.get_username(self)
        password = Registration.get_passsword(self)
        Database.profile[username] = password
        Registration.get_phone_number(self)
        return username, password, True

    """================================================================================"""
    def registration_status(self):
        username, password, registration = self.sign_up()
        if registration:
            print("Your account has been created")
            print(f"Your password is {Database.profile[username]}")
            Database.new_account.append(username)
        else:
            print("Registration failed")

    """================================================================================"""
    def login(self):
        login, username = Login.sign_in(self)

        if login:
            time.sleep(1)
            print("Sign in successful")
        else:
            print("Sign in failed")

    """================================================================================"""
    def new_password(self):
        while True:
            username = input("Enter your username: ")
            if username in Database.user_name_list:
                break
            else:
                print("username not found!")
        reset_password = Password.reset_password(self)

        if username:
            if reset_password:
                print("Password Changed Successfully")
                print("WELCOME to cyber9ja.com.ng")

            else:
                print("Password change unsuccessful")

    """================================================================================"""
    def show_all_products(self):
        for product, price in Shop.stock_price.items():
            if product in Shop.stock.keys():
                print(f"{Shop.stock[product]} pieces of {product} available at ${price} each")

    def add_to_stock_inventory(self):  # Add new product to stock
        product = input("Enter product name: ").lower()
        quantity = int(input(f"Quantity: "))
        Shop.new_stock_addition(self, product, quantity)

    def add_new_product(self):
        product = input("Enter product name: ").lower()
        quantity = int(input(f"Quantity: "))
        price = int(input("Enter price: "))
        Shop.new_product(self, product, quantity, price)

    def change_product_price(self):
        product = input("Enter product name: ").lower()
        price = int(input(f"Enter new price for {product}: "))
        Shop.edit_product_price(self, product, price)

    """================================================================================"""
    def store(self):
        Buy.total(self)

    """================================================================================"""

    def run(self):
        self.display_menu()
        while True:
            choice = input("Enter an option: ")
            if choice == "0":
                self.quit()
            elif choice == "1":
                self.registration_status()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.new_password()
            elif choice == "4":
                self.shopping_menu()
                while True:
                    option = input("\nEnter an option: ")
                    if option == "1":
                        self.show_all_products()
                    elif option == "2":
                        self.add_to_stock_inventory()
                    elif option == "3":
                        self.add_new_product()
                    elif option == "4":
                        self.change_product_price()
                    elif option == "0":
                        break
                    else:
                        print(f"{option} is an invalid input")
                        self.shopping_menu()
            elif choice == "5":
                self.store()
            else:
                print(f"{choice} is an invalid input")
                self.display_menu()

            print()

    def quit(self):
        print("Thanks for shopping!")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()

