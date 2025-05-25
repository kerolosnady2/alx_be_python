x = input("Enter your monthly income: ")
input_one = int(x)
y = input("Enter your total monthly expenses: ")
input_two = int(y)
monthly_income = input_one - input_two
print("Your monthly savings are $",monthly_income)
projected_savings = monthly_income * 12 + (monthly_income * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",int(projected_savings))
