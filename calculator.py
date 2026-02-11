def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


def menu():
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (**)")
    print("6. Modulus (%)")
    print("7. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    while True:
        menu()
        choice = input("Choose an option (1-7): ")

        if choice == "7":
            print("Goodbye")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid option. Try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            print("Result:", divide(num1, num2))

        elif choice == "5":
            print("Result:", power(num1, num2))

        elif choice == "6":
            print("Result:", modulus(num1, num2))


if __name__ == "__main__":
    main()
