#LOg in
username = "avanikim"
password = "ferrarif2002"

user = input("Input USERNAME ---> ")
passw = input("Input PASSWORD ---> ")

if user == username and passw == password:
    print("=====================Succesfully Loged in=====================")

else:
    print("Invalid username or password. Try again")
    exit()

#Loanee's informatins
loanee_first_name = input("Enter your first name ---> ")
loanee_job_description = input("Enter your job description ---> ")
collateral_description = input("Enter your collateral/s ---> ")
collateral_value = eval(input("Enter your collateral/s value ---> "))

#Collateral value checking
if collateral_value >= 30000:
    print("Your collateral has met the minimum requirement for getting a loan")
    print(" ")
    print("You may now proceeed")

else:
    print("Your collateral has not met the minimun requirment eligable for getting a loan")
    exit()

#Age verification
age = int(input("Enter your age ---> "))

if age >= 21 and age <= 65:
    print("Age accepted")

else:
    print("We're deeply sorry, your age is not eligable for gettng a loan")
    exit()

#further questions
is_employed = bool(input("Are you currently employed? "))
credit_score = eval(input("Credit Score History ---> "))
annual_income = eval(input("How much is your annual income---> "))
has_collateral = bool(input("Do you have any collateral? "))

if is_employed == True:
    print("Great!")

    if credit_score >= 750:

        base_interest_rate_tier1 = 5.0

        if annual_income >= 100000:
            interest_rate_tier1 = base_interest_rate_tier1 - 0.5
        else:
            interest_rate_tier1 = base_interest_rate_tier1

        interest_rate = interest_rate_tier1

        print("Pwede na sa", interest_rate_tier1, "% interest")

    elif credit_score >= 600 and credit_score < 750:

        base_interest_rate_tier2 = 8.0

        if annual_income < 40000:
            interest_rate_tier2 = base_interest_rate_tier2 + 1.5
        elif has_collateral == True:
            interest_rate_tier2 = base_interest_rate_tier2 - 1.0
        else:
            interest_rate_tier2 = base_interest_rate_tier2

        interest_rate = interest_rate_tier2

        print("Pwede na sa", interest_rate_tier2, "% interest")

    elif credit_score < 600:
        print("Sayang! Credit score too low")
        exit()

#final step (amount to loan)

loan_amount = int(input("Enter the amount you want to loan ---> "))

interest_amount = loan_amount * (interest_rate / 100)
total_payment = loan_amount + interest_amount

print(" ")
print("==========LOAN RECEIPT==========")
print("Loanee:", loanee_first_name)
print("Job:", loanee_job_description)
print("Collateral/s:", collateral_description)
print("Collateral/s value:", collateral_value)
print("Loan amount:", loan_amount)
print("Calculated interest rate:", interest_rate, "%")
