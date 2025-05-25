x = input("Enter your monthly income: ")
input_one = int(x)
y = input("Enter your total monthly expenses: ")
input_two = int(y)
monthly_saving = input_one - input_two
print("Your monthly savings are $",monthly_saving)
projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",int(projected_savings))
