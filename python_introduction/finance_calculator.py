monthly_income = input("Enter your monthly income:")
monthly_expense = input ("Enter your total monthly expenses:")

monthly_savings =float (monthly_income) - float(monthly_expense)
projected_savings = float(monthly_savings) * 12 + (float(monthly_savings) *12 *0.05)

prfloat(f"Your monthly savings are {monthly_savings}")
prfloat (f"Projected savings after one year, with floaterest, is: {projected_savings}")
