class Shop:
    stock_price = {
        "apple": 2, "pineapple": 1.2, "rice": 0.4, "milk": 0.8,
        "coke": 1.6, "juice": 0.7, "biscuit": 0.1, "pot": 0.6,
        "mask": 0.5, "orange": 0.3, "banana": 0.14, "potato": 1,
        "strawberry": 0.2, "bread": 1.2, "carrot": 0.2, "egg": 0.3
    }
    stock = {
        "apple": 100, "pineapple": 100, "rice": 100, "milk": 100,
        "coke": 100, "juice": 100, "biscuit": 100, "pot": 100,
        "mask": 100, "orange": 100, "banana": 100, "potato": 100,
        "strawberry": 100, "bread": 100, "carrot": 100, "egg": 100
    }

    def new_stock_addition(self, product, quantity):   # Add stock to inventory store
        if product in self.stock:
            for key, value in self.stock.items():
                if key == product:
                    self.stock[key] += quantity
                    break
        else:
            print(f"{product} not in stock")

    def new_product(self, product, quantity, price):
        if product in self.stock and product in self.stock_price:
            print(f"{product} in stock.")

        else:
            self.stock[product] = quantity
            self.stock_price[product] = price

    def edit_product_price(self, product, new_price):
        if product in self.stock_price.keys():
            for key, value in self.stock_price.items():
                if key == product:
                    self.stock_price[key] = new_price
                    break
        else:
            print(f"{product} not in stock.")



