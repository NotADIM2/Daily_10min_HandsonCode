print("======== Mini Calculator ====  ")

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            exit()
    else:
        print("Error: Invalid operator.")
        exit()

    print(f"The result of {num1} {operator} {num2} is: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    print("Thank you for using the Mini Calculator!")