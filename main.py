import random
import time
shop_stats = {"money": 100 , "total_revenue": 0 , "total_profit": 0 , "experience": 0 , "reputation": 50, "level": 1}
shop_inventory = {"apple" : {"stock": 10 , "cost": 1 , "price": 2},
                "banana" : {"stock": 6 , "cost": 3 , "price": 5},
                "orange" : {"stock": 13 , "cost": 1 , "price": 2}
                }


def menu():
    print("=====SHOP======")
    print("1. View Shop Inventory")
    print("2. View Shop Stats")
    print("3. Buy Stock")
    print("4. Open Shop")
    print("5. Quit")

def view_shop_inventory():
    for i , (product , financials) in enumerate(shop_inventory.items() , start = 1):
        print(f"{i}.{product.title()} (Stock: {financials["stock"]} left) = Cost: RM{financials["cost"]}, Price: RM{financials["price"]}")
    print("Successfully viewed your shop's inventory!\n")
        
def view_shop_stats():
    for stat, value in shop_stats.items():
        print(f"{stat.title()}: {value}")
    print("Successfully viewed your shop's stats!\n")

def buy_stock():
    print("===Stock Shop===")
    print("1. Apple | Cost: RM 1 ")
    print("2. Banana | Cost: RM 3 ")
    print("3. Orange | Cost: RM 1 ")

    option = input("What would you like to buy?(1-3): ")

    products = list(shop_inventory.keys())
    product = products[int(option) - 1]

    if option in ("1" or "2" or "3"):
        try:
            amount = int(input(f"How many {product.title()} would you like to buy? "))
            if amount <= 0:
                print("Invalid amount!")
            elif shop_stats["money"] >= shop_inventory[product]["cost"] * amount:
                shop_stats["money"] -= shop_inventory[product]["cost"] * amount
                shop_inventory [product]["stock"] += amount
                shop_stats ["experience"] += 2 * amount
                print(f"Successfully bought {amount} {product.title()}\n")
            else:
                print("You don't have enough money! Go earn some money!\n")

        except ValueError:
            print("Enter a valid number!\n")
    else:
        print("Invalid option!\n")

def customer_interaction():
    print("1. Serve customer")
    print("2. Reject customer")
    print("3. Close shop")
    
def open_shop():
    print("Your shop is open!")
    while True:
        print("Waiting for customer...")
        if 80 < shop_stats["reputation"] <= 100: 
            wait_time = random.randint(1,3)
        elif 50 < shop_stats["reputation"] <= 79: 
            wait_time = random.randint(2,5)
        elif 20 < shop_stats["reputation"] <= 49: 
            wait_time = random.randint(3,7)
        elif 10 < shop_stats["reputation"] <= 19: 
            wait_time = random.randint(4,8)
        else:
            wait_time = random.randint(5,10)

        time.sleep(wait_time)

        print("A customer entered your shop!")

        product = random.choice(list(shop_inventory.keys()))
        amount = random.randint(1,15)
        suffix = "" if amount == 1 else "s"
        print(f"This customer wants {amount} {product.title()}{suffix}")

        customer_interaction()
        option = input("What will you do? ")

        if option == "1":
            if shop_inventory[product]["stock"] >= amount:
                revenue = shop_inventory[product]["price"] * amount
                profit = shop_inventory[product]["price"] * amount - shop_inventory[product]["cost"] * amount
                shop_inventory[product]["stock"] -= amount
                shop_stats["reputation"] = max(shop_stats["reputation"] + 10 , 0)
                shop_stats["money"] += revenue
                shop_stats["total_revenue"] += revenue
                shop_stats["total_profit"] += profit
                print(f"Successfully served customer! You earned RM{revenue}\n")
            else:
                shop_stats["reputation"] = max(shop_stats["reputation"] - 5 , 0)
                print(f"You don't have enough {product.title()} stock!")
                print("The customer left! They left a bad review!")
        elif option == "2":
            print("The customer left! They left a bad review!")
            shop_stats["reputation"] = max(shop_stats["reputation"] - 10 , 0)
        elif option == "3":
            print("You closed your shop!")
            break
        else:
            print("Invalid option!")
            

def main():
    while True:
        menu()
        option = input("Enter your option(1-4): ")

        if option == "1":
            view_shop_inventory()
        elif option == "2":
            view_shop_stats()
        elif option == "3":
            buy_stock()
        elif option == "4":
            open_shop()
        elif option == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option!\n")

main()