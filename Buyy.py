from Shopping_Store import Shop

# Calculate sub total
# Apply discount to total price


class Buy:
    items_dict = {}
    subtotal_price = 0

    def user_status_menu(self):
        print("""
    STATUS STRUCTURE
    B. Bronze User
    S. Silver User
    G. Gold User
        """)

    # Get items and quantity
    def items_quantity(self, item_dict):
        print("List the items you are buying with their respective quantities")
        while True:
            print()
            item = input("Item: ")
            if item == "0":
                break
            elif item in Shop.stock.keys():
                quantity = int(input("Quantity: "))
                if Shop.stock[item] >= quantity:
                    Shop.stock[item] -= quantity
                    self.items_dict[item] = quantity
                else:  # The remaining
                    print(f"{item} remains {Shop.stock[item]} pieces in stock")
            else:
                print("Item not in stock.")

        return item_dict

    def calculate_subtotal(self):
        sum = 0
        items_dict = self.items_quantity(self.items_dict)
        for item, quantity in items_dict.items():
            if item in Shop.stock_price.keys():
                print(f"{item}: ${Shop.stock_price[item]} x {quantity} = ", end = " ")
                sum = Shop.stock_price[item] * quantity
                print(f"${sum}")
            self.subtotal_price += sum

        return self.subtotal_price

    def bronze_discount(self, subtotal_cost):
        discount = 25
        discount_price = (25 / 100) * subtotal_cost
        total_cost = subtotal_cost - discount_price
        print(f"\n{discount}% off for Bronze membership at total price not less than $100")
        print(f"Total price is ${float(total_cost)}")

    def silver_discount(self, subtotal_cost):
        discount = 35
        discount_price = (35 / 100) * subtotal_cost
        total_cost = subtotal_cost - discount_price
        print(f"\n{discount}% off for Silver membership at total price not less than $100")
        print(f"Total price is ${float(total_cost)}")

    def gold_discount(self, subtotal_cost):
        discount = 50
        discount_price = (50 / 100) * subtotal_cost
        total_cost = subtotal_cost - discount_price
        print(f"\n{discount}% off for Gold membership at total price not less than $100")
        print(f"Total price is ${float(total_cost)}")

    def total(self):
        subtotal = self.calculate_subtotal()
        if subtotal <= 100:
            print(f"Total price is ${subtotal}")
        else:
            status = input("\nWhat's your status: ")
            if status == "B" or status == "b":  # You get 25% discount
                print(f"Price before discount is ${subtotal}")
                self.bronze_discount(subtotal)
            elif status == "S" or status == "s":  # You get 35% discount
                print(f"Price before discount is ${subtotal}")
                self.silver_discount(subtotal)
            elif status == "G" or status == "g":  # You get 50% discount
                print(f"Price before discount is ${subtotal}")
                self.gold_discount(subtotal)
            else:
                print("Choice is an invalid input")


if __name__  == "__main__":
    b = Buy()
    b.total()






