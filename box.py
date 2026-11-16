

for x in range (5):
    for y in range (5):
        if x== 0 or x== 5 - 1 or y == 0 or y == 5 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

