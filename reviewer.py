#inputs
age = int(input("Enter your age ---> "))
reven = float(input("Enter monthly revenue ---> $"))
crdts = int(input("Enter your credit score ---> "))
yrsinb = int(input("years in business ---> "))
hasdef = bool(input("Def history ---> "))
colls = input("Enter your collateral ---> ")
coll_val = float(input("Collateral value ---> $"))

max_loan = 0
base_fee = 0.0
#baseline
if age >= 21 and yrsinb >= 2 and hasdef:
    print("Baseline requirement pass")

    max_loan = reven * 3
    print("max loan for high crdit score is ", max_loan)
    print("high credit score of 720")
    base_fee - 0.0

    #tier1
    if crdts >= 720: 
        print("high credit score of 720")
        if reven >= 5000:
            base_fee = max_loan * 0.02
            print("base fee rate is ", base_fee)
        else: 
            base_fee = max_loan * 0.025
            print("base fee rate is ", base_fee)
        #collateral
        if coll_val >= max_loan:
            print("Collateral", colls, "--Accepted")
        else: 
            print("Collateral not Accepted")

        #surcharge
        surcharge = max_loan * base_fee
        if coll_val % 5000 != 0:
            surcharge += 250

    #tier2
    elif crdts <= 620 and crdts <720: 
        max_loan = reven * 1.5
        print("max loan is set to ", max_loan)
        if yrsinb >= 5:
            base_fee = max_loan * 0.02
            print("base fee rate is ", base_fee)
        else:
            base_fee = max_loan *0.035
            print("base fee rate is ", base_fee)

        if coll_val >= max_loan:
            print("Collateral", colls, "--Accepted")
        else: 
            print("Collateral not Accepted")

    #tier3
    elif crdts < 620:
        print("Not tier 1")

else: 
    print("REJECTED: High risk application or ineligable")
