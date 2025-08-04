print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Exit")

option = int(input("Choose an operation: "))

if option == 5:
    print("You chose to exit.")
    exit()
elif option in [1, 2, 3, 4]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if option == 1:
        result = num1 + num2
        print(f"Addition of {num1} and {num2} is: {result}")

    elif option == 2:
        result = num1 - num2
        print(f"Subtraction of {num1} and {num2} is: {result}")

    elif option == 3:
        result = num1 * num2
        print(f"Multiplication of {num1} and {num2} is: {result}")

    elif option == 4:
        if num2 != 0:
            result = num1 / num2
            print(f"Division of {num1} by {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
else:
    print("Invalid option.")
