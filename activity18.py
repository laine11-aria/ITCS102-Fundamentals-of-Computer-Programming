#boolean variable
sasama = True

while sasama == True:
    ask = input("Do you wish to continue? (yes/no) ----> ")

    if ask.lower() == "yes":
        print("Continuing")
        continue
    else:
        print("Stopping now...")
        break