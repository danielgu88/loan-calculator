import argparse
import sys
import math

MINIMUM_PARAMETERS = 5
MONTHS_IN_YEAR = 12

def check_negative_parameters():
    if args.payment is not None:
        if float(args.payment) < 0:
            return True

    if args.principal is not None:
        if float(args.principal) < 0:
            return True

    if args.periods is not None:
        if float(args.periods) < 0:
            return True

    if args.interest is not None:
        if float(args.interest) < 0:
            return True

    return False

def diff_formula(principal, periods, interest, month_number):
    return (principal / periods) + interest * (principal - (principal * (month_number - 1) / periods))

def annuity_formula_right_side(interest, periods):
    return (interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if ((args.type != "annuity" and args.type != "diff") or args.type is None) or \
        (args.type == "diff" and args.payment is not None) or args.interest is None \
        or len(sys.argv) < MINIMUM_PARAMETERS or check_negative_parameters():
    print("Incorrect parameters")
else:
    interest = float(args.interest) / 1200
    overpayment = 0

    if args.type == "annuity":
        if args.payment is None:
            principal = float(args.principal)
            periods = float(args.periods)

            monthly_payment = math.ceil(principal * annuity_formula_right_side(interest, periods))
            overpayment = math.ceil(monthly_payment * periods - principal)

            print("Your annuity payment = {}!".format(monthly_payment))
            print("Overpayment = {}".format(overpayment))
        elif args.principal is None:
            annuity_payment = float(args.payment)
            periods = float(args.periods)

            principal = math.ceil(annuity_payment / annuity_formula_right_side(interest, periods))
            overpayment = math.ceil(annuity_payment * periods - principal)

            print("Your loan principal = {}!".format(principal))
            print("Overpayment = {}".format(overpayment))
        else:
            principal = float(args.principal)
            monthly_payment = float(args.payment)

            periods = math.ceil(math.log(monthly_payment / (monthly_payment - interest * principal), 1 + interest))

            output = ""
            if periods < MONTHS_IN_YEAR:
                output = str(periods) + " months"
            elif periods == MONTHS_IN_YEAR:
                output = "1 year"
            else:
                years = int(periods / MONTHS_IN_YEAR)
                months = periods - years * MONTHS_IN_YEAR

                if months == 0:
                    output = "{} years".format(years)
                else:
                    output = "{} years and {} months".format(years, months)

            overpayment = math.ceil(monthly_payment * periods - principal)

            print("It will take {} to repay this loan!".format(output))
            print("Overpayment = {}".format(overpayment))
    else:
        for i in range(1, int(args.periods) + 1):
            monthly_payment = math.ceil(diff_formula(float(args.principal), float(args.periods), interest, i))
            overpayment += monthly_payment

            print("Month {}: payment is {}".format(i, monthly_payment))

        overpayment -= float(args.principal)
        overpayment = math.ceil(overpayment)

        print("\nOverpayment = {}".format(overpayment))
