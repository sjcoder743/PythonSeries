def sum_of_even_odd(n):
    even_sum = 0
    odd_sum = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    return even_sum, odd_sum

# Input the value of n
n = int(input("Enter the value of n: "))

# Calculate the sum of even and odd integers
even_sum, odd_sum = sum_of_even_odd(n) 

# Print the results
print(f"Sum of even integers from 1 to {n}: {even_sum}")
print(f"Sum of odd integers from 1 to {n}: {odd_sum}")
