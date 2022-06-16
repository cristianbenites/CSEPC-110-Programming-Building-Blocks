"""
Title: Meal Price Calculator
Author: Cristian Benites

Description:
    This program simulates a restaurant's cashier. 
    It starts by defining the costs of the services and then shows a menu with 3 options:
        1 - Register a new sale
        2 - Close the cashier
        3 - Redefine the costs of the services

    Observation: I learned many things from this project.
    I know that the requirements where for a simpler implementation, but I took this assignment
    as an opportunity to challenge myself and do something cool.
"""

from time import sleep

"""
Stores the cashier for all entries
"""
class Cashier:
    def __init__(self) -> None:
        self._cash = 0.0;

    @property
    def cash(self):
        return self._cash

    def add_cash(self, amount):
        self._cash += amount

    def close_cashier(self):
        final_value = self._cash
        self._cash = 0.0;
        return final_value


"""
Sets an entry with the meal costs and makes the proper calculation
"""
class Entry:
    def __init__(self, childs_meal, adults_meal, dessert_price, juice_price, sales_tax_rate):
        self.childs_meal = childs_meal
        self.adults_meal = adults_meal
        self.dessert_price = dessert_price
        self.juice_price = juice_price
        self.sales_tax_rate = sales_tax_rate
        self.number_of_children = 0;
        self.number_of_adults = 0;
        self.number_of_juices = 0;
        self.number_of_desserts = 0;

    def define_number_of_children(self):
        number = input('Insert the number of children: ')
        self.number_of_children = 0 if number == '' else int(number)

    def define_number_of_adults(self):
        number = input('Insert the number of adults: ')
        self.number_of_adults = 0 if number == '' else int(number)

    def define_number_of_juices(self):
        number = input('Insert the amount of juices: ')
        self.number_of_juices = 0 if number == '' else int(number)

    def define_number_of_desserts(self):
        number = input('Insert the amount of desserts: ')
        self.number_of_desserts = 0 if number == '' else int(number)

    def get_subtotal(self):
        return (
            self.childs_meal * self.number_of_children +
            self.adults_meal * self.number_of_adults +
            self.juice_price * self.number_of_juices +
            self.dessert_price * self.number_of_desserts
        )

    def get_sales_tax(self):
        return self.get_subtotal() * (self.sales_tax_rate / 100)

    def get_total(self):
        return self.get_subtotal() + self.get_sales_tax()

    # Receives the payment amount, returns the change and restores the meal registers
    def finalize_sale(self, payment_amount) -> float:
        change = payment_amount - self.get_total()
        self.number_of_children = 0
        self.number_of_adults = 0
        self.number_of_juices = 0
        self.number_of_desserts = 0

        return change
"""
The Calulator is the core of the system.

It initiates by instancing the menu options,
a boolean to check if the system should keep running,
and instantiate a new Cashier to be used.

The after instancing the Calculator class, you can initialize the calculator by running the run() method.

The run() method is the core function that offers an interface to all interations with the calculator.

The config() method is responsible to build a new Entry object and setup its parameters.

The menu() method is an interface of options to access other Calculator methods. It expects an input from user,
checks if it is correct an then executes the proper method.

The new_sale() function, registers a new entry sale, prints all of the costs,
receives the payment and returns the change. After a new sale is registered, it adds to the Cashier.

Finally, the close_cashier() method, close the cashier and
properly prints the final balance, ending the execution of the script.
"""
class Calculator:
    def __init__(self) -> None:
        self.menu_options = {
            '1': 'self.new_sale',
            '2': 'self.close_cashier',
            '3': 'self.config',
        }
        self.system_is_running = True
        self.cashier = Cashier()

    # Builds a new Entry object.
    def config(self) -> None:
        print("--------------------------")
        print(" Configure the parameters ")
        print("--------------------------")

        childs_meal_price = float(input('Please, insert the price of a child\'s meal: '))
        adults_meal_price = float(input('Insert the price of an adult\'s meal: '))
        dessert_price = float(input('Insert the price an individual dessert: '))
        juice_price = float(input('Insert the price for a juice: '))
        sales_tax_rate = float(input('Insert the sales tax rate (in %): '))

        self.entry = Entry(childs_meal_price, adults_meal_price, dessert_price, juice_price, sales_tax_rate)
        sleep(0.5)

    # Prints a menu and receives an option
    def menu(self):
        print("----------------------------")
        print(f"CASHIER: ${self.cashier.cash:,.2f}")
        return input(f"Choose from the options below:\n 1. New meal entry\n 2. Close cashier\n 3. Configure the parameters (change meal prices)\n>> ")

    def new_sale(self):
        self.entry.define_number_of_children()
        self.entry.define_number_of_adults()
        self.entry.define_number_of_juices()
        self.entry.define_number_of_desserts()

        sales_total = self.entry.get_total()

        print("----------------------------")
        print(f"Subtotal: ${self.entry.get_subtotal():,.2f}")
        print(f"Sales tax: ${self.entry.get_sales_tax():,.2f}")
        print(f"Sales total: ${sales_total:,.2f}")
        print("----------------------------")

        payment_amount = float(input('What is the payment amount? '))
        
        change = self.entry.finalize_sale(payment_amount)

        self.cashier.add_cash(payment_amount)

        print("")
        print("Payment registered successfully!")
        print(f"Change: ${change:,.2f}")
        print("")

        sleep(1)

    def close_cashier(self):
        self.system_is_running = False

        print("----------------------------\n")
        print("          THANK YOU         \n")
        print(f"The final balance is: ${self.cashier.close_cashier():,.2f}")
        print("----------------------------\n")
        
    def run(self):
        print("Welcome to the Meal Price Calculator!")
        print("To get started, set up meal prices.")
        self.config()


        while(self.system_is_running):
            option = self.menu() 
            action = self.menu_options.get(option)

            if action:
                eval(action + '()')

calculator = Calculator()
calculator.run()
