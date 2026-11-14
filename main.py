import random
import time
shop_stats = {"money": 100 , "total_revenue": 0 , "total_profit": 0 , "experience": 0 , "reputation": 50, "level": 1}
shop_inventory = {"apple" : {"stock": 0 , "cost": 1 , "price": 2},
                "banana" : {"stock": 0, "cost": 3 , "price": 5},
                "orange" : {"stock": 0 , "cost": 1 , "price": 2}
                }


def menu():
    print("=====SHOP======")
    print("1. View Shop Inventory")
    print("2. View Shop Stats")
    print("3. Buy Stock")
    print("4. Open Shop")
    print("5. Tutorial")
    print("6. Quit")

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

    if option == "1" or option == "2" or option == "3":
        products = list(shop_inventory.keys())
        product = products[int(option) - 1]
        try:
            amount = int(input(f"How many {product.title()} would you like to buy? "))
            if amount <= 0:
                print("Invalid amount!")
            elif shop_stats["money"] >= shop_inventory[product]["cost"] * amount:
                shop_stats["money"] -= shop_inventory[product]["cost"] * amount
                shop_inventory [product]["stock"] += amount
                shop_stats ["experience"] += 1 * amount
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
                shop_stats["reputation"] = min(shop_stats["reputation"] + 10 , 100)
                shop_stats["money"] += revenue
                shop_stats["total_revenue"] += revenue
                shop_stats["total_profit"] += profit
                shop_stats["experience"] += 5
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

def tutorial():
    print("===== TUTORIAL =====")
    print("Welcome, shop owner! Your goal is to build a successful shop by earning money and keeping your customers happy.")
    print("1. Buy Stock")
    print("- Purchase apples, bananas and oranges. \n- Each product has its own cost and selling price.")
    print("2. Open Your Shop")
    print("- Customers will arrive automatically.\n- Serve them if you have enough stock.\n- Reject them or close your shop if needed.")
    print("3. Manage Your Finances")
    print("- Money: Your available cash.\n- Revenue: Total earnings from sales.\n- Profit: Earnings after deducting product costs.")
    print("4. Maintain Your Reputation")
    print("- Serving customers increases reputation.\n- Rejecting customers or running out of stock decreases it.\n- Higher reputation means customers arrive faster!")

def level_up():
    xp_needed = 100 + (shop_stats["experience"] + 25)

    if shop_stats["experience"] >= xp_needed:
        shop_stats["level"] += 1
        shop_stats["experience"] -= xp_needed
        print(f"Your store has leveled up to level {shop_stats['level']}!")

def save_stats():
    with open ("shop stats.txt" , "w") as file:
        for stats, value in shop_stats.items():
            value = str(value)
            file.write(stats + ":" + value + "\n")

def load_stats():
    try:
        with open ("shop stats.txt" , "r") as file:
            for line in file:
                parts = line.strip().split(":")
                stats = parts[0]
                value = parts[1]
                shop_stats[stats] = int(value)
    except FileNotFoundError:
        pass
        
def save_stock():
    with open("shop stocks.txt" , "w") as file:
        for product , details in shop_inventory.items():
            file.write(product + "|" + str(details["stock"]) + "|" + str(details["cost"]) + "|" + str(details["price"]) + "\n")

def load_stock():
    try:
        with open ("shop stocks.txt" , "r") as file:
            for line in file:
                parts = line.strip().split("|")
                product = parts[0]
                stock = parts [1]
                cost = parts [2]
                price = parts [3]

                shop_inventory[product] = {"stock": int(stock), "cost" : int(cost) , "price": int(price)}
    except FileNotFoundError:
        pass


def main():
    load_stats()
    load_stock()
    while True:
        menu()
        option = input("Enter your option(1-6): ")

        if option == "1":
            view_shop_inventory()
        elif option == "2":
            view_shop_stats()
        elif option == "3":
            buy_stock()
            save_stock()
            level_up()
        elif option == "4":
            open_shop()
            save_stats()
            save_stock()
            level_up()
        elif option == "5":
            tutorial()
        elif option == "6":
            print("Thanks for playing!")
            save_stats()
            save_stock()
            break
        else:
            print("Invalid option!\n")

main()