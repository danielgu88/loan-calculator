import math

monthly_payment = 0
last_payment = 0

principal = int(input("Enter the loan principal:\n"))
selection = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:\n""")

if selection == "m":
    monthly_payment = int(input("Enter the monthly payment:\n"))
    months_to_repay = math.ceil(principal / monthly_payment)

    s = "s"

    if months_to_repay == 1:
        s = ""

    print("\nIt will take {} month{} to repay the loan".format(months_to_repay, s))
else:
    months = int(input("Enter the number of months:\n"))

    monthly_payment = math.ceil(principal / months)
    last_payment = principal - (months - 1) * monthly_payment

    if last_payment == monthly_payment:
        print("\nYour monthly payment = {}".format(monthly_payment))
    else:
        print("\nYour monthly payment = {} and the last payment = {}.".format(monthly_payment, last_payment))
