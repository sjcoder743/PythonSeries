def print_left_aligned_pyramid(rows):
    for i in range(1, rows + 1):
        # Print @ symbols
        for k in range(i):
            print("@", end="")
        
        # Move to the next line after each row
        print()

# Set the number of rows for the left-aligned pyramid
num_rows = int(input("Enter numbr of rows: "))

# Call the function to print the left-aligned pyramid
print_left_aligned_pyramid(num_rows)
