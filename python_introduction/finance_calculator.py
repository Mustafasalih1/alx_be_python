monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your expenses: "))
monthly_savings = float(monthly_income) - float(monthly_expenses)
annual_savings = monthly_savings * 12
project_savings = annual_savings + (annual_savings * 0.05)
print("your monthly savingis","$", monthly_savings)
print("Projected savings after one year, with interest, is:$", project_savings)