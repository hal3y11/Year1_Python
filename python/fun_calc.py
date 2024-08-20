def add(x, y):
    result = x + y
    print(f"The sum of {x} and {y} is: {result}")

def subtract(x, y):
    result = x - y
    print(f"The difference of {x} and {y} is: {result}")

def multiply(x, y):
    result = x * y
    print(f"The product of {x} and {y} is: {result}")

def divide(x, y):
    if y != 0:
        result = x / y
        print(f"The division of {x} by {y} is: {result}")
    else:
        print("Cannot divide by zero")

def remainder(x, y):
    if y != 0:
        result = x % y
        print(f"The remainder of {x} divided by {y} is: {result}")
    else:
        print("Cannot calculate remainder when dividing by zero")

num1 = input("Enter the first integer: ")
num2 = input("Enter the second integer: ")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")

    choice = int(input("Choose an operation (1-5): "))

    if choice == 1:
        add(num1, num2)
    elif choice == 2:
        subtract(num1, num2)
    elif choice == 3:
        multiply(num1, num2)
    elif choice == 4:
        divide(num1, num2)
    elif choice == 5:
        remainder(num1, num2)
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")
else:
    print("Invalid input.")
