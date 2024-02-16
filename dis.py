sales = int(input("Enter sales : "))
print(sales)

if sales >= 10000:
    discount = sales - (sales * 10 / 100)
elif sales < 10000 and sales >= 5000:
    discount = sales - (sales * 5 / 100)
else:
    print("There is no discount")

    print("Final price of the sale is : ", sales)
