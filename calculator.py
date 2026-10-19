def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        try:
            result = divide(num1, num2)
        except ZeroDivisionError as e:
            print(e)
            return
    else:
        print("Invalid operation selected.")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    calculator()
