
# Simple Calculator Program


while True:
    print("\n========== SIMPLE CALCULATOR ==========")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (Remainder %)")
    print("6. Exponentiation (Power **)")

    # Get user's choice
    choice = input("Enter your choice (1-6): ")

    # Check if the choice is valid
    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice. Please select a number between 1 and 6.")
        continue

    # Get input numbers from the user
    try:
        num1 = float(input("ENTER THE FIRST NUMBERR: "))
        num2 = float(input("ENTER THE SECOND NUMBER: "))
    except ValueError:
        print("INVALID INPUT \n. Please enter numeric values.")
        continue

    # Perform the operation based on the user's choice
    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error:\n Cannot divide by zero.")
    elif choice == '5':
        print("Result:", num1 % num2)
    elif choice == '6':
        print("Result:", num1 ** num2)

    # Ask if the user wants to perform another calculation
    again = input("\nDo you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break
