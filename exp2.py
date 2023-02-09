def tax(income):
    if income > 250_000 and income <= 400_000:
        tax = income * 0.15
    elif income > 400_000 and income <= 800_000:
        tax = income * 0.2 + 22_500
    elif income > 800_000 and income <= 2_000_000:
        tax = income * 0.25 + 102_500
    elif income > 2_000_000 and income <= 8_000_000:
        tax = income * 0.3 + 402_500
    elif income > 8_000_000:
        tax = income * 0.35 + 2_202_500
    else:
        tax = 0
    return tax

income = float(input("Enter Annual Income: "))
print('')

if tax(income) == 0:
    print("No tax on your Annual Income")
    print('')
else:
    print("The tax on your Annual Income is: Php {:,}".format(tax(income)))

netIncome = income - tax(income)
print("Your Net Income amounts to: Php {:,}".format(netIncome))