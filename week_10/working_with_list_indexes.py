shopping_list = []
item = ''

print("Please enter the items of the shopping list (type: quit to finish):")
while item != 'quit':
    item = input("Item: ")
    if(item != 'quit'):
        shopping_list.append(item)

print("\n\nThe shopping list is:")
for item in shopping_list:
    print(item)

print("\n\nThe shopping list with indexes is: ")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")

index_to_change = int(input("\n\nWhich item would you like to change? "))
new_item = input("What is the new item? ")
shopping_list[index_to_change] = new_item

print("\n\nThe shopping list with indexes is: ")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")
