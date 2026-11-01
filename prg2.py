while True:
    number1 = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    number2 = float(input("Enter the second number: "))

    if operation == "+":
        answer = number1 + number2
    elif operation == "-":
        answer = number1 - number2
    elif operation == "*":
        answer = number1 * number2
    elif operation == "/":
        answer = number1 / number2
    else:
        print("Invalid operation")
        continue

    print("Answer =", answer)

    again = input("Do you want to calculate again? (yes/no): ")

    if again.lower() != "yes":
        print("Calculator closed.")
        break