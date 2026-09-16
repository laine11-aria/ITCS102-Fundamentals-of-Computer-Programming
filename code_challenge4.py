username = "avanikim"
password = "ferrarif2002"

user = input("Input USERNAME ---> ")
passw = input("Input PASSWORD ---> ")

if user == username and passw == password:
	print("=====================Succesfully Loged in=====================")

else:
    print("Invalid username or password. Try again")
    exit()


loanee_first_name = input("Enter your first name ---> ")
loanee_job_description = input("Enter your job description ---> ")
collateral_description = input("Enter your collateral/s ---> ")
collateral_value = eval(input("Enter your collateral/s value ---> "))


if collateral_value >= 30000:
    print("Your collateral has met the minimum requirement for getting a loan")
    

else:
    print("Your collateral has not met the minimun requirment eligable for getting a loan")
    exit()
    



age = int(input("Enter your age ---> "))
is_employed = bool(input("Are you currently employed? "))
credit_score = eval(input("Credit Score History ---> "))
annual_income = eval(input("How much is your annual income---> "))
has_collateral = bool(input("Do you have any collateral? "))


if age >= 21 and age <= 65 and is_employed == True:
    if credit_score >= 750:

        base_interest_rate_tier1 = 5.0

        if annual_income >= 100000:
            interest_rate_tier1 = base_interest_rate_tier1 - 0.5
        else:
            interest_rate_tier1 = base_interest_rate_tier1

        print("Pwede na sa", interest_rate_tier1, "% interest")

    elif credit_score >= 600  and age <750 :
        base_interest_rate_tier2 = 8.0

        if annual_income < 40000:
            interest_rate_tier2 = base_interest_rate_tier2 + 1.5
        elif has_collateral == True:
            interest_rate_tier2 = base_interest_rate_tier2 - 1.0
        else:
            interest_rate_tier2 = base_interest_rate_tier2

        print("Pwede na sa", interest_rate_tier2, "% interest")

    elif credit_score < 600:
        print("Sayang! Credit score too low")

else:
    print("We're deeply sorry, your age is not eligable for loan")