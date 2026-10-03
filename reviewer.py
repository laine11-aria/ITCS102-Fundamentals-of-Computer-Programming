age = int(input("Enter your age ---> "))
reven = float(input("Enter monthly revenue ---> "))
crdts = int(input("Enter your credit score ---> "))
yrsinb = int(input("years in business ---> "))
hasdef = bool(input("Def history ---> "))
colls = input("Enter your age ---> ")
coll_val = float(input("Collateral value"))

max_loan = 0
base_fee = 0.0
#baseline
if age >= 21 and yrsinb >= 2 and hasdef == False:
    print("Baseline requirement pass")

    max_loan = reven * 3
    print("max loan for high crdit score is ", max_loan)
    print("high credit score of 720")
    base_fee - 0.0
    if crdts >= 720: #tier1
        print("high credit score of 720")
        if reven >= 5000:
            base_fee = max_loan *0.02
            print("base fee rate is ", base_fee)
        else: 
            base_fee = max_loan * 0.025:
            print("base fee rate is ", base_fee)


    elif crdts <= 620 and crdts <720: #tier2
        max_loan = reven * 1.5
        if yrsinb >= 5:
            base_fee = max_loan * 0.02
            print("base fee rate is ", base_fee)
        else:
            base_fee = max_loan *0.035
            print("base fee rate is ", base_fee)
    elif crdts < 620:
        print("Credit score too low for loan")

else: 
    print("REJECTED: High risk application or ineligable")