def print_number_triangle(rows):
    for i in range(1, rows + 1):
        # Print the repeated number
        for j in range(i):
            print(i, end=" ")
        
        # Move to the next line after each row
        print()

# Set the number of rows for the number triangle
num_rows = int(input("Enter rows: "))

# Call the function to print the number triangle
print_number_triangle(num_rows)
