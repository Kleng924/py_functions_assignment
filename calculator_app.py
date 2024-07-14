# 1. The Calculator App
# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, 
# multiplication, and division.


# Task 1: Create functions for each arithmetic operation.

def add(n1, n2):
    result = n1 + n2
    return result

num1 = int(input("Put number 4:"))
num2 = int(input("Put number 8:"))

print(add(num1, num2))

def sub(n1, n2):
    result = n1 - n2
    return result

num1 = int(input("Put number 8:"))
num2 = int(input("Put number 4:"))

print(sub(num1, num2))

def mul(n1, n2):
    result = n1 * n2
    return result

num1 = int(input("Put number 8:"))
num2 = int(input("Put number 4:"))

print(mul(num1, num2))

def div(n1, n2):
    result = n1 / n2
    return result

num1 = int(input("Put number 16:"))
num2 = int(input("Put number 4:"))

print(div(num1, num2))


# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

def perform_operations():
    operation = input("What operation would you like to use? (add, subtract, multipy, divide): ").strip().lower()

    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number."))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operation.")
        return
    
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")

perform_operations()

#Task 3: Ensure your program can handle division by zero and other potential errors.
# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, 
# there is error handling set up to prevent an error from showing in the console.

def divide_numbers(n1, n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both arguments must be numbers."
    except Exception as e:
        return f"An unexpected error occured: {e}"
    else:
        return result

print(divide_numbers(12, 6))
print(divide_numbers(12, 0))
print(divide_numbers(12, "a"))
print(divide_numbers(12, None))