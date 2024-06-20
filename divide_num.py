def divide_num():
    try:
        # Get input from the user
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))

        # Perform the division
        result = dividend / divisor
        print("The result is:", {result})

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Division complete.")

# Perform the division
divide_num()