sales = int(input("Enter sales: "))

if sales>=10000:
  dis = int(sales - (sales * 10/100))
elif sales<10000 and sales >=5000:
  dis = int(sales - (sales * 5/100))
else: 
  print("Opps... There is no discount for less then 5000")

print("Final price After discount is : ", dis)  