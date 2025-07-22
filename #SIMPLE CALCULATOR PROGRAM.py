#SIMPLE CALCULATOR PROGRAM

while True:
    print("\n======SIMPLE CALCULATOR======")
    print("SELECT AN OPERATIION TO PERFORM")
    print("1. ADDITION(+)")
    print("2. SUBTRACTION(-)")
    print("3. MULTIPLICATION(*)")
    print("4. DIVISION(/)")
    print("5. MODULUS(REMAINDER %)")
    print("6. EXPONENTIAL (**)")

#INPUT CHOICE
choice = input("ENTER YOURE CHOICE 1-6: ")
if choice not in['1', '2', '3', '3', '4', '5', '6']:
    print("Invalid\n plese select a number btw 1-6")
    continue

try:
    num1 = float(input("Enter the first number:: "))
    num2 = float(input("Enter the second number:: "))
except value error:
    print("invalid data input. \n please enter a numerical value. ")
    continue

#algebric operations
if choice == '1':
    print("Result: ",num1 + num2)
if choice == ''2:
    print("Result: ",num1 - num2)
if choice == '3':
    print("Result: ",num1 * num2)
if choice == '4':
    if num != 0:
    `   print("Result: ",num1 / num2)
    else:
        print("error. cannot divide by zero.")
if choice == '5':
    print("Result: ",num1 % num2)
if choice == '6':
    print("Result: ",num1 ** num2)

#performing operation again
again = i9nputy("\n Do you want to perform the calculation again? (yes/no): ")
if again.lower() != 'yes':
    print("thank you\n Goodbye")
    break