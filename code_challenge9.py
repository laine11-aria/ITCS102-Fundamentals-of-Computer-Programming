#task1
MP = int(input("Enter loan amount ---> $"))
Yrs = int(input("Enter peiod of years ---> "))


months = Yrs * 12
rem_bal = MP
interest_rate = 0.00256

for blue in range(1, 25):


    principal = 41.67
    interest = rem_bal * interest_rate
    monthly_payment = principal + interest

    rem_bal = rem_bal - principal

    print(f"{blue}\t | ${round(monthly_payment, 2)}\t | {round(interest, 2)}\t |{principal}\t | {round(rem_bal, 2)}")

print()
print("\n")

#task2
for red in range(7):
    for yellow in range(1, 14):
        if red + yellow == 7 or yellow - red == 7 or red == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()
print("\n")

#task3
for white in range(5):
    for black in range(5):
        if white + black == 4 or white == 0 or white == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()