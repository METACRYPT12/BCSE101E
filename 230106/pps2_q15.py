import datetime

seats = [12, 3]
main_registry = []


class passenger:
    def __init__(self, name, age, dest, date, total_fare, booking_type):
        self.name = name
        self.age = age
        self.dest = dest
        self.date = date
        self.total_fare = total_fare
        self.booking_type = booking_type


def cred_verify():
    user = input("Username: ")
    passw = input("Password: ")
    with open("230106\credentials.txt", mode='r') as creds:
        if (user == creds.readline().strip() and passw == creds.readline().strip()):
            creds.close()
            return
        print("Invalid Credentials")
        creds.close()
        exit()


def fare_retrieve(destination):
    if (destination == "Hosur"):
        return 75
    elif (destination == "Vaniyambadi"):
        return 250
    elif (destination == "Vellore"):
        return 500
    elif (destination == "Walaja"):
        return 600
    elif (destination == "Chennai"):
        return 750
    else:
        print("Destination not Found")
        exit()


def differnce(diff):
    diff = int(diff)
    if (diff < 4):
        return 0
    elif (diff < 7):
        return 0.50
    elif (diff < 14):
        return 0.80
    elif (diff < 20):
        return 0.90
    else:
        return 1


def booking():

    print("\nA. Regular ({0} seats)\nB. Tatkal ({1} seats)\n".format(
        seats[0], seats[1]))
    print(f"\nFare details from Bangalore\n------------\nRegular:\n\nHosur Rs75\nVaniyambadi Rs 250\nVellore Rs 500\nWalaja Rs600\nChennai Rs750\n\n* for senior citizen 10 % concession(Age 60 and above)\n\nTatkal Booking fare - Rs100 addition to the regular fare\n")
    option = input()
    tatkal_fare = 0
    if (option == "A" and seats[0] > 0):
        tatkal_fare = 0
    elif (option == "B" and seats[1] > 0):
        tatkal_fare = 100
    else:
        print("\nSeats not available on selected option!\n")
        return

    n = int(input("No. of Passengers: "))
    if (option == "A"):
        seats[0] = seats[0] - n
    else:
        seats[1] = seats[1] - n
    i = 0
    psngr = []
    print("Passenger Details (name age): ")
    while (i < n):
        psngr.append(input().split())
        i = i + 1
    destination = input("Destination: ")
    date = input("Enter Date of Travel (dd mm yyyy): ").split()
    date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
    i = 0
    name = []
    age = []
    fare = fare_retrieve(destination)
    total_fare = tatkal_fare
    while (i < n):
        name.append(psngr[i][0])
        age.append(int(psngr[i][1]))
        total_fare = total_fare + fare if age[i] < 60 else .9*fare
        i = i + 1
    main_registry.append(
        passenger(name, age, destination, date, total_fare, option))
    print_details()


def cancellation():
    print(f"\nCancellation Refund Details\n----------------------------\n20 days before the date of journey - full refund\n2 weeks before the date of journey - 90 % fare refund\n1 week  before the date of journey - 80 % fare refund\n4 days  before the date of journey - 50 % fare refund\n< 4 days - No refund\n")
    reference_date = datetime.datetime(2022, 11, 15)
    psngr = input("Passenger Details (name age): ").split()
    date_of_cancellation = input(
        "Enter Date of Cancellation (dd mm yyyy): ").split()
    date_of_cancellation = datetime.datetime(int(date_of_cancellation[2]), int(
        date_of_cancellation[1]), int(date_of_cancellation[0]))
    psngr[1] = int(psngr[1])
    for obj in main_registry:
        diff = obj.date - date_of_cancellation
        diff_fare = differnce(diff.days)
        for names, ages in zip(obj.name, obj.age):
            if (psngr[0] == names and psngr[1] == ages):

                tmp = fare_retrieve(
                    obj.dest) if ages < 60 else .9*fare_retrieve(obj.dest)
                obj.total_fare = obj.total_fare - diff_fare*tmp
                print("\nRefund: {}\n".format(diff_fare*tmp))
                obj.name.pop(obj.name.index(names))
                obj.age.pop(obj.age.index(ages))
                if (obj.booking_type == "A"):
                    seats[0] = seats[0] + 1
                else:
                    seats[1] = seats[1] + 1
    print_details()


def print_details():
    seat_no = 15
    f = open(r"230106\reservation.txt", mode="w")
    f.seek(0)
    f.write(("\nA. Regular({0} seats)\nB. Tatkal({1} seats)\n".format(
        seats[0], seats[1])))
    for obj in main_registry:
        print("\n")
        for names, ages in zip(obj.name, obj.age):
            print("{0} - {1} - Bengaluru - {2} - {3}".format(names,
                  ages, obj.dest, seat_no))
            f.write("{0} - {1} - Bengaluru - {2} - {3}\n".format(names,
                    ages, obj.dest, seat_no))
            seat_no = seat_no - 1
        f.write("\nTotal Fare: {}\n\n".format(obj.total_fare))
        print("Total Fare", obj.total_fare)


cred_verify()
while (True):
    print("\n\nMain Menu\n---------")
    print("1. Booking\n2. Cancellation\n3. Exit\n")
    option = int(input())
    if (option == 1):
        booking()
    elif (option == 2):
        cancellation()
    elif (option == 3):
        exit()
