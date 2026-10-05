s
#Inputs
owner_age = int(input("Input age: "))
monthly_revenue = float(input('Your Monthly Revenue: '))
credit_score = int(input("Your Credit_score: "))
years_in_business = float(input('How many years are you in the business? '))
has_defaults = bool(input("Had previous default/bankruptcy? "))
collateral_name = input("Type of Collateral: "))
collateral_value = float(input("Value of your Collateral: "))

max_limit = 0
base_fee = 0.0
#Baseline Requirements
if owner_age >= 21 and years_in_business and has_defaults == False:
    print("Passed Baseline Requirement")

    max_limit = monthly_revenue * 3
    print("max loan for high credit score is ", max_limit)
    print("highb credit score of 720")
    base_fee = 0.0

    #tier 1
    if credit_score >= 720:
        print("high credit sore of 720")
        if monthly_revenue >= 5000:
            base_fee = max_limit * 0.015
            print("base rate is ", base_fee)
        else:
            base_fee = max_limit * 0.025
            print("base rate is ", base_fee)
        #collateral 
        if collateral_value >= max_limit:
            print("Collateral ", collateral_name, "--Accepted")
        else:
            print("Collateral not accepted")

        #surcharge
        surcharge = max_limit * base_fee
        if collateral_value % 5000 != 0:
            surcharge += 250

    #tier 2
    elif credit_score <= 620 and credit_score <720:
        max_limit = monthly_revenue * 1.5
        print("max loan is set to ", max_limit)
        if years_in_business >= 5:
            base_fee = max_limit * 0.02
            print("base fee rate is ", base_fee)
        else:
            base_fee = max_limit * 0.035
            print("base fee rate is ", base_fee)

        if collateral_value >= max_limit:
            print("Collateral ", collateral_name, "--Accepted")
        else:
            print("Collateral not accepted")
    #tier 3
    elif credit_score < 620:
        print("Credit score too low for a loan")
    else:
        print("Not tier 1")

else:
    print("Rejected: High Risk Application or Ineligible Owner")





