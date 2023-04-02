# Mahbub is quite dumb at programming, be patient while reading the code. Contact him in Telegram @linuxhasan
# I welcome your contribution to this piece of junk

## Added input validation, with better error handling
## Added instructions on how to use it
## Added more descriptive errors

print(
    "How to use: \nEnter your EMI total amount, how many months do you want to pay off your EMI in (3,6,12,24,36), interest rate (in percentage), processing fee (in percentage) and minimum processing fee. It will calculate your EMI and your first EMI with processing fee included. \n\nFor example: Enter total amount: 10000 \nIn how many months do you want to pay off: 12, \nWhat is the interest rate in percentage: 11 \nWhat is the processing fee in percentage?: 2.95 \nWhat is the minimum processing fee?: 575. \n\nNote: From processing fee and minimum processing fee, whichever is bigger, will be added to calculation."
)


def Amount():
    while True:
        amount = input("Enter total amount: ")
        try:
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Amount must be higher than", amount)
        except Exception:
            print("Please enter numbers only. Decimals are allowed")

    return amount


def EmiMonth():
    while True:
        emi_month = input("In how many months do you want to pay off?: ")
        try:
            emi_month = int(emi_month)
            if emi_month > 0:
                break
            else:
                print(
                    "EMI Month should be higher than 0 (usual terms are 3,6,12,24,36 months)"
                )
        except Exception:
            print(
                "Please enter integers only (no decimals). For example: 3, and not 3.5"
            )

    return emi_month


def InterestRate():
    while True:
        interest_rate = input("What is the interest rate in percentage?: ")
        try:
            interest_rate = float(interest_rate)
            if interest_rate > 0:
                break
            else:
                interest_rate = 0
                break
        except Exception:
            print("Please enter numbers only. Decimals are allowed")

    return interest_rate


def ProcessingFee():
    while True:
        try:
            processing_fee = float(input("What is the processing fee in percentage?: "))
            if processing_fee > 0:
                break
            else:
                processing_fee = 0
                break
        except Exception:
            print("Please enter numbers only. Decimals are allowed")

    return processing_fee


def MinProcFee():
    while True:
        try:
            min_proc_fee = float(input("What is the minimum processing fee?: "))
            if min_proc_fee > 0:
                break
            else:
                min_proc_fee = 0
                break
        except Exception:
            print("Please enter numbers only. Decimals are allowed")

    return min_proc_fee


def main():
    amount = Amount()
    emi_month = EmiMonth()
    interest_rate = InterestRate()
    processing_fee = ProcessingFee()
    min_proc_fee = MinProcFee()

    if interest_rate == 0:
        EMIValue = amount / emi_month
    else:
        Interest = interest_rate / 12 / 100
        EMIValue = (
            amount
            * Interest
            * (1 + Interest) ** emi_month
            / ((1 + Interest) ** emi_month - 1)
        )

    print("Your payable monthly installment is: %.2f" % EMIValue)

    processing_fee_amount = EMIValue / 100 * processing_fee

    if processing_fee_amount > min_proc_fee:
        EmiWithProcFee = EMIValue + processing_fee_amount
    else:
        EmiWithProcFee = EMIValue + min_proc_fee

    print(
        "Your first EMI installment with processing fee will be: %.2f" % EmiWithProcFee
    )


if __name__ == "__main__":
    main()
