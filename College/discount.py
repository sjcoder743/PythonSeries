def calculate_discount(sales):
    if sales >= 10000:
        discount_percentage = 0.10
    elif sales < 1000:
        discount_percentage = 0.05
    else:
        discount_percentage = 0
    discount = sales * discount_percentage
    discounted_price = sales - discount

    return discount, discounted_price

# Get total sales from the user
try:
    total_sales = float(input("Enter the total sales amount: $"))
    
    # Check if the input is valid (a positive number)
    if total_sales >= 0:
        discount, discounted_price = calculate_discount(total_sales)
        
        # Display the results
        print(f"\nOriginal Sales: ${total_sales}")
        print(f"Discount Percentage: {discount * 100}%")
        print(f"Discount: ${discount}")
        print(f"Discounted Price: ${discounted_price}")
    else:
        print("Please enter a valid positive number for total sales.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
