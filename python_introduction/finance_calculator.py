monthly_income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your expenses: "))
monthly_savings = monthly_income - expenses
print("your monthly savingis","$", monthly_savings)
interest = 0.05
savings_after_one_year = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is:$", savings_after_one_year)