"""
Title: W05 Prepare - Checkpoint: If Statements
"""

x = int(input("Type a number: "))
y = int(input("Another number: "))

if x > y:
    print("The first number is greater.")
else:
    print("The first number is not greater.")

if x == y:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

if x < y:
    print("The second number is greater.")
else:
    print("The second number is not greater.")

my_fav_animal = "dog"

users_fav_animal = input("What is your favorite animal? ")

if users_fav_animal.lower() == my_fav_animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite")
