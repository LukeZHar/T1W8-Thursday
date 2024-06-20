def convert_to_int(value):
    try:
        result = int(value)
        print(f'Conversion Successful! Result: {result}')
    except ValueError:
        print('Conversion Failed! Enter a valid integer value.')
    finally:
        print('Closing any open resources.')

# User_input
user_input= input("Enter a number to convert to int: ")

# Convert the number
convert_to_int(user_input)