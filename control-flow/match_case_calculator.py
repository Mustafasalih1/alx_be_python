first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
if operation == "+":
    result = first_number + second_number
    print("The result is", result)
elif operation == "-":
    result = first_number - second_number
    print("The result is",result)
elif operation == "*":
    result = first_number * second_number
    print("The result is", result)
elif operation == "/" and second_number != 0:
    result = first_number / second_number
    print("The result is", result)
elif operation == "/" and second_number == 0:
        print("Cannot divide by zero.")