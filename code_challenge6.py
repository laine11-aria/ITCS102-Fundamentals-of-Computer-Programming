
size = int(input("Inpur size of x ---> "))

for x in range(size):
    for y in range(size):
        if x + y == size-1 or x==y :
            print("*", end = "")
        else:
            print("", end= " ")
    print()