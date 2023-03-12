# EMI Calculator

def emiCalc():
  
    print("Note: If you use it to calculate 0% interest EMIs, then enter 0 as interest rate, processing fee and also minimum processing fee")
    
    TotalValue = float(input("How much is the total price you want to convert to EMI?: ৳"))
    InterestRate = float(input("How much is the interest rate in percentage?: "))
    EmiMonth = float(input("How many months for the EMI payoff?: "))
    ProcessingFee = float(input("How much is the processing fee in percentage?: "))
    MinProcessingFee = float(input("How much is the minimum processing fee?: ৳"))

    if 0 >= InterestRate:
        TotalValueWithInterest = TotalValue
    elif 0 < InterestRate:
        p = TotalValue
        n = EmiMonth
        r = InterestRate / 12 / 100
        EmiAmount = p * r * (1+r) ** n / ((1+r) ** n - 1)
    
    EmiRemainder = EmiAmount % EmiMonth
    print("Your EMI amount is: ৳%.2f" % EmiAmount, "(EMI remainder is: ৳%.2f" % EmiRemainder, ")")
    
    FstEmiProcFee = EmiAmount / 100 * ProcessingFee

    if FstEmiProcFee > MinProcessingFee:
        FstEmiProcFeeTotal = FstEmiProcFee + EmiAmount
    else:
        FstEmiProcFeeTotal = EmiAmount + MinProcessingFee

    print("Your First EMI with processing fee is: ৳%.2f" % FstEmiProcFeeTotal)

    return EmiAmount

emiCalc()
