
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operation = input("Enter the operation (+, -, *, /): ")


if operation == '+':
    result = num1 + num2
    print(f"\nThe result of addition is: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"\nThe result of subtraction is: {result}")
elif operation == '*':
    result = num1 * num2
    print(f"\nThe result of multiplication is: {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\nThe result of division is: {result}")
    else:
        print("\nError: Division by zero is not allowed.")
else:
    print("\nInvalid operation. Please choose +, -, *, or /.")
