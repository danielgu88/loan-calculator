import math

MONTHS_IN_YEAR = 12

def formula_right_side(interest, periods):
    return (interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)

selection = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n""")

if selection == "n":
    principal = int(input("Enter the loan principal:\n"))
    monthly_payment = int(input("Enter the monthly payment:\n"))
    interest = float(input("Enter the loan interest:\n")) / 1200

    periods = math.ceil(math.log(monthly_payment / (monthly_payment - interest * principal), 1 + interest))

    output = ""
    if periods < MONTHS_IN_YEAR:
        output = str(periods) + " months"
    elif periods == MONTHS_IN_YEAR:
        output = "1 year"
    else:
        years = int(periods / MONTHS_IN_YEAR)
        months = periods - years * MONTHS_IN_YEAR

        output = "{} years and {} months".format(years, months)

    print("It will take {} to repay this loan!".format(output))
elif selection == "a":
    principal = int(input("Enter the loan principal:\n"))
    periods = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n")) / 1200

    monthly_payment = math.ceil(principal * formula_right_side(interest, periods))
    print("Your monthly payment = {}!".format(monthly_payment))
else:
    annuity_payment = float(input("Enter the annuity payment:\n"))
    periods = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n")) / 1200

    principal = math.ceil(annuity_payment / formula_right_side(interest, periods))
    print("Your loan principal = {}!".format(principal))
