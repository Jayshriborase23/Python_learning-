# Python Exception Handling

# 1. Basic try-except
try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Please enter a valid number.")


# 2. Handling Division by Zero
try:
    a = 10
    b = 0
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")


# 3. try-except-else
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)


# 4. try-except-finally
try:
    number = int(input("Enter another number: "))
    print("Square:", number ** 2)

except ValueError:
    print("Invalid input.")

finally:
    print("Program execution completed.")


# 5. Multiple Exceptions
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Division:", a / b)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Second number cannot be zero.")
