def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero"

def main():
    print("Select operation to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if choice == '1':
            print(f"The result is: {addition(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiplication(num1, num2)}")
        elif choice == '4':
            result = division(num1, num2)
            print(f"The result is: {result}")
    else:
        print("Invalid choice! Please choose a valid operation.")

if __name__ == "__main__":
    main()
