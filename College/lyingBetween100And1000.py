# Get input from the user
user_input = input("Enter a number: ")

# Check if the input is a valid integer
if user_input.isdigit():
    user_number = int(user_input)
    # Check if the number is between 100 and 1000
    if 100 <= user_number <= 1000:
        print(f"The number {user_number} is between 100 and 1000.")
    else:
        print(f"The number {user_number} is not between 100 and 1000.")
else:
    print("Invalid input. Please enter a valid integer.")
