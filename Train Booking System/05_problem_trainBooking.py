import time

secretCode = 2506


class trainApp:
    seats = 1
    trainFair = 399

    def bookTicket(self):
        print("Enter your name : ", end="")
        input()
        print("Age : ", end="")
        int(input())
        print("Sex : ", end="")
        input()
        print("Aadhar number : ", end="")
        input()
        print()
        time.sleep(1)
        print("Checking Aadhar...")
        print()
        time.sleep(4)
        print("Aadhar Verified")
        time.sleep(3)
        print()
        print("Processing...........")
        print()
        time.sleep(5)
        print("Checking Status....")
        print()
        time.sleep(2)
        if (self.seats == 0):
            print("Booking Uncessful")
            print()
            time.sleep(1)
            print("SORRY there is no vacancy in the train")
        else:
            print("Booking Done")
            print()
            time.sleep(1)
            print("Your Seat is confirmed.")
            self.seats = self.seats - 1

    def status(self):
        print("Current Status :-")
        print(f"Seats remaining : {self.seats}")

    def info(self):
        print(f"The train fair is Rs {self.trainFair}")
        print()


operation = trainApp()


def mainroot():
    print()
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print()
    print("WELCOME TO INDIAN RAILWAYS")
    print()
    print("--------------------------")
    print("1. Check info")
    print("2. Booking Status")
    print("3. Book Ticket")
    print("--------------------------")
    print()
    print("Print the following numbers (1,2 or 3) to choss the particular operations")
    choose = int(input())
    print()
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print()

    if (choose == 1):
        operation.info()
        print()
        print("Press 999 for Main Menu")
        print("Press any key to exit")
        print("Enter the Secret Key to deactivate the Site (for officials only)")
        print()
        choose01 = int(input())
        if (choose01 == 999):
            mainroot()
        elif (choose01 == secretCode):
            print()
            print("The site is Deactivated Succesfully")
            print()
            exit()
        else:
            print()
            print("Operation Ended")
            print()
            print("Thanks for visiting INDIAN RAILWAY")
            time.sleep(10)
            mainroot()

    elif (choose == 2):
        operation.status()
        print()
        print("Press 999 for Main Menu")
        print("Press any key to exit")
        print("Enter the Secret Key to deactivate the Site (for officials only)")
        print()
        choose01 = int(input())
        if (choose01 == 999):
            mainroot()
        elif (choose01 == secretCode):
            print()
            print("The site is Deactivated Succesfully")
            print()
            exit()
        else:
            print()
            print("Operation Ended")
            print()
            print("Thanks for visiting INDIAN RAILWAY")
            time.sleep(10)
            time.sleep(10)
            mainroot()

    elif (choose == 3):
        operation.bookTicket()
        print()
        print("Press 999 for Main Menu")
        print("Press any key to exit")
        print("Enter the Secret Key to deactivate the Site (for officials only)")
        print()
        choose01 = int(input())
        if (choose01 == 999):
            mainroot()
        elif (choose01 == secretCode):
            print()
            print("The site is Deactivated Succesfully")
            print()
            exit()
        else:
            print()
            print("Operation Ended")
            print()
            print("Thanks for visiting INDIAN RAILWAY")
            time.sleep(10)
            mainroot()

    else:
        print("INVALID OPERATIONS")
        print()
        print("Press 999 for Main Menu")
        print("Press any key to exit")
        print("Enter the Secret Key to deactivate the Site (for officials only)")
        print()
        choose01 = int(input())
        if (choose01 == 999):
            mainroot()
        elif (choose01 == secretCode):
            print()
            print("The site is Deactivated Succesfully")
            print()
            exit()
        else:
            print()
            print("Operation Ended\n")
            print()
            print("Thanks for visiting INDIAN RAILWAY")
            time.sleep(10)
            mainroot()


mainroot()
