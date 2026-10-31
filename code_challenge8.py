rows = int(input("Enter rows ---> "))


for blue in range(1, rows +1 , +1):
    for yellow in range(rows - blue):
        print(" ", end= "")
    for yellow in range(blue):
        print("* ", end="")
    print()

for red in range(rows - 1, 0, -1):
    for white in range (rows - red):
        print(" ", end= "")
    for white in range(red):
        print("* ", end="")
    print()

