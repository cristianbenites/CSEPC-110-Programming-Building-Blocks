from time import sleep

# We use sleep just to improve the user's experience.
# We use it inside each action instead of the while loop, because by doing so, 
# we can have more control of "sleeping" when is more appropriate

class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.prices = []
        self.system_is_running = True

    def get_menu_action(self):
        print(f"\nYour current list has {len(self.products)} item{'s' if len(self.products) != 1 else ''}.")
        print("Select one of the following:\n"
            "1. Add item\n"
            "2. View cart\n"
            "3. Remove item\n"
            "4. Compute total\n"
            "5. Quit\n")
        return input("Please, enter an action: ")

    def run_next_step(self, action):
        match action:
            case "1":
                return self.add_item()
            case "2":
                return self.view_cart()
            case "3":
                return self.remove_item()
            case "4":
                return self.compute_total()
            case "5":
                return self.quit()
            case _:
                print("Invalid option.")
                sleep(1)
    
    def add_item(self):
        item = input("What item would you like to add? ")

        try:
            price = float(input(f"What is the price of \"{item}\"? "))

            self.products.append(item)
            self.prices.append(price)
            print(f"\"{item}\" has been added to the cart.")

            sleep(1)
        except:
            print("The price should be a number")

    def view_cart(self):
        print("The contents of the shopping cart are: ")
        print("ITEM                              PRICE")
        for index, product in enumerate(self.products):
            print(f"{index + 1}. {product.capitalize(): <30} - ${self.prices[index]:,.2f}")
        sleep(1)

    def remove_item(self):
        self.view_cart()

        try:
            item = int(input("Which item would you like to remove? "))
            item = item - 1

            self.products.pop(item)
            self.prices.pop(item)
            print("Item removed.")
            sleep(1)
        except:
            print("Wrong value inserted. Please type the number of the item in the list.")

    def compute_total(self):
        total = 0;
        for price in self.prices:
            total += price

        print(f"The total price of the items in the shopping cart is ${total:,.2f}")
        sleep(1)

    def quit(self):
        print("Thank you. Goodbye.")
        self.system_is_running = False

    def run(self):
        print("Welcome to the Shopping Cart!")
        while(self.system_is_running):
            action = self.get_menu_action()
            self.run_next_step(action)


shopping_cart = ShoppingCart()
shopping_cart.run()
