price_dict = {"apple": 5, "pineapple": 7, "rice": 4, "milk": 8,
              "coke": 6, "juice": 5, "biscuit": 3, "pot": 6,
              "mask": 0.5, "orange": 0.3, "banana": 4, "potato": 1,
              "strawberry": 2, "bread": 2, "carrot": 0.2, "egg": 0.3
              }

discount_dict = {"B": 95, "S": 85, "G": 75}

# Get list of items and quantity the user wants to buy


def update_price_dictionary(get_price_dict):
    product = input("Product: ")
    price = float(input("New price: "))
    price_dict[product] = price

    return price_dict
def get_user_goods_and_quantity(get_price_dict):
    buying_dict = {}
    print("Enter 'Q' or 'q' to stop placing order.")
    while True:
        print()
        product = input("Product: ")
        if product == 'Q' or product == 'q':    # If the user enters Q or q, stop placing order
            break
        else:
            if product in get_price_dict:
                quantity = int(input(f"How many pcs/kg/bottle of {product}? "))
                buying_dict[product] = quantity
            else:
                print(f"{product} is not available at the moment.")
    return buying_dict

def get_price_before_discount(get_price_dict):
    get_buying_dict = get_user_goods_and_quantity(price_dict)
    get_subtotal_price = 0
    set_membership = ""
    print()
    for good in get_buying_dict.keys():
        sum = 0
        if good in get_price_dict.keys():
            sum += get_price_dict[good] * get_buying_dict[good]
            print(f"{good.title()}: ${get_price_dict[good]} x {get_buying_dict[good]} = ${sum}")
        get_subtotal_price += sum
    return get_subtotal_price

def get_discount(get_discount_dict):
    subtotal_price = get_price_before_discount(price_dict)
    # Get membership status
    if subtotal_price > 100:
        membership = input("\nMembership status('B' for 'Bronze, 'S' for 'Silver', 'G' for 'Gold'? ").title()
        if membership in get_discount_dict.keys():
            if membership == "B":
                set_membership = "Bronze"
                total_price = get_discount_dict[membership]/100 * subtotal_price
                discount = 100 - get_discount_dict[membership]
                print(f"\n{discount}% off for {set_membership} member at total price not less than $100")
                print(f"Total price is ${float(total_price)}")

            elif membership == "S":
                set_membership = "Silver"
                total_price = get_discount_dict[membership]/100 * subtotal_price
                discount = 100 - get_discount_dict[membership]
                print(f"\n{discount}% off for {set_membership} member at total price not less than $100")
                print(f"Total price is ${float(total_price)}")

            elif membership == "G":
                set_membership = "Gold"
                total_price = get_discount_dict[membership]/100 * subtotal_price
                discount = 100 - get_discount_dict[membership]
                print(f"\n{discount}% off for {set_membership} member at total price not less than $100")
                print(f"Total price is ${float(total_price)}")
        else:
            print("Invalid input")

    else:
        print(f"\nTotal price is ${float(subtotal_price)}")

get_discount(discount_dict)











