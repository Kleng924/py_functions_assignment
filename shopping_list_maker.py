# The Shopping List Maker
# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a function to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

def manage_list():
    items = []

    def add_item(item):
        items.append(item)
        print(f'Added: {item}')
        print(f'Current list: {items}')

    def remove_item(item):
        if item in items:
            items.remove(item)
            print(f'Removed: {item}')
        else:
            print(f'Item "{item}" not found in the list.')
        print(f'Current list: {items}')

    while True:
        action = input("Enter 'add' to add an item, 'remove' to remove an item, or 'done' to exit: ").lower()
        
        if action == 'done':
            break
        elif action == 'add':
            item = input("Enter the item to add: ")
            add_item(item)
        elif action == 'remove':
            item = input("Enter the item to remove: ")
            remove_item(item)
        else:
            print("Invalid action. Please enter 'add', 'remove', or 'done'.")

    print("Final list:", items)

manage_list()






# Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to 
# continue to add, remove, and print off their shopping list until they decide to "quit", also known as breaking 
# the loop.