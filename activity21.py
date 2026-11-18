
#part1

passengers = ["Ana", "Ben", "Carla"]

passengers.append("Dan")
print(passengers)
passengers.insert(0, "Lola")
print(passengers)

passengers.remove("Ben")
print(passengers)
x = passengers.pop()
print(passengers)
y = passengers.pop(0)
print(passengers)
len(passengers)
print(passengers)
print()
"Ana" in passengers
print(passengers)

passengers.reverse()
print(passengers)

print()
print()
print()

#part2
print("JEEPNEY SIMULATOR INTERACTIVE")
print()

route = ["Terminal", "Perez Park", "Pacific Mall"]
passengers = []
SEATS = 6
FARE = 13
total = 0

while True:
    print()
    print('Sakay:', passengers)
    print(len(passengers), 'of', SEATS, 'seats')
    print('1 Sakay  2 Priority seat  3 Para po!')
    print('4 Baba sa pinto  5 Baba sa harap')
    print('6 Seat check  7 Balikan  8 Exit')
    choice=input('Choice ')


    
    if choice == '1':
        if len(passengers) == SEATS:
            print('Puno na!')
        else:
            name = input('Name: ')
            passengers.append(name)
            total = total + FARE
            print(name, 'Boarded at the Back.')


    elif choice == '2':
        if len(passengers) == SEATS:
            print('Puno Na!')
        else:
            name=input('Name: ')
            passengers.insert(0, name)
            total = total + FARE
            print(name, 'took the priority seat.')
    

    elif choice == '3':
        name=input('Who is getting off?: ')
        if name in passengers:
            passengers.remove(name)
            print(name, 'got off, INGAT!')
        else:
            print(name, 'is not on this Jeep!')


    elif choice == '4':
        if len(passengers)==0:
            print('Jeepney is empty.')
        else:
            left=passengers.pop()
            print(left, 'got off at the door')


    elif choice == '5':
        if len(passengers) == 0:
            print('The Jeepney is empty.')
        else:
            front=passengers.pop(0)
            print(front, "got off at the front.")


    elif choice == '6':
        for i in range (len(passengers)):
            print('Seat', i + 1, passengers[i])


    elif choice == '7':
        route.reverse()
        print('Route:', route)


    elif choice == '8':
        print('Total fare today:', total)
        break


    else:
        print('Invalid Choice')

