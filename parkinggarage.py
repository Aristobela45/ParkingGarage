# This project is a pair programming project. This means, that one person(The driver) will code the project while the other people(The navigators)will brainstorm and guide to a working solution.
# Each of you should share/switch these roles every 30mins-1hr (-- Or you may elect to switch "drivers" after creating specific methods of the class).

# The Initial Driver needs to Make sure to:
# create a local folder for the project, create a github repository, commit the inital files, share the link

# Both navigators should then:
# fork the code, clone it and begin.

# The current driver MUST share their screen so the navigators can help brainstorm to a working solution.

# When code has been updated, you will need to pull down the changes.

# Your parking gargage class should have the following methods (SUGGESTIONS):
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary


import random


class Parkinggarage():
    def __init__(self):
        self.ticketsav = ["1", "2", "3", "4", "5"]
        self.parkingspace = ["1", "2", "3", "4", "5"]
        self.currenttickets = {}

    def ticketTaker(self):
        if self.ticketsav == []:
            print("Sorry parking garage is full. Please come back later. ")
            return Parkinggarage()
        print("We have up to 5 spaces available when we're vacant. ", self.ticketsav)
        num = (input("Please enter in a ticket number from 1-5: "))
        while num not in self.ticketsav:
            print("\nSorry that number is not available. ")
            print("The available spaces are: ", self.ticketsav)
            num = (input("Please enter a valid number"))
        self.ticketsav.remove(num)
        self.parkingspace.remove(num)
        self.currenttickets[num] = ""
        print("Thank you for parking with us! ")

    def payingTicket(self):
        if self.currenttickets == {}:
            print("Garage is empty. ")
            return Parkinggarage()
        num = input("What is your ticket number: ")
        while num not in self.currenttickets.keys():
            print("Error: Ticket not found, please enter a valid ticket number: [{}]".format(",".join(str(
                t) for t in sorted([int(key) for key in self.currenttickets.keys()]))))  # this line may not work
            num = input("Enter valid ticket ")
        if self.currenttickets[num] == "paid":
            print("Thanks for paying for your ticket! ")
            return Parkinggarage()
        amount = (input("Please insert $15: "))
        while amount.isdigit() == False:
            amount = (input("Sorry, that's not a valid response. "))
        if float(amount) < 15:
            amount = float(input("Please insert $15: "))
        if float(amount) == 15:
            print("Thank you for paying for your ticket. ")
        if float(amount) > 15:
            print("Thanks for the extra money. ")
        if num in self.currenttickets.keys():
            self.currenttickets[num] = "paid"
            print("Ticket has been paid, have a nice day! ")

    def leaving(self):
        if self.currenttickets == {}:
            print("Sorry, garage is empty.")
            return Parkinggarage()
        num = input("What is your ticket number: ")
        while num not in self.currenttickets.keys():
            print("Error: Ticket not found, please enter a valid ticket number: [{}]".format(
                ",".join(str(t) for t in sorted([int(key) for key in self.currenttickets.keys()]))))
            num = input("What is your ticket number? ")
        while self.currenttickets[num] != "paid":
            amount = input("Sorry, you need to insert $15")
            while amount.isdigit() == False:
                amount = (input("Sorry, that's not the right amount. "))
            if float(amount) < 15:
                amount = float(input("Please enter an amount of $15"))
                self.currenttickets[num] = "paid"
            if float(amount) == 15:
                print("Thank you! ")
                self.currenttickets[num] = "paid"
            if float(amount) > 15:
                print("Thanks for the extra money. ")
                self.currenttickets[num] = "paid"
        del self.currenttickets[num]
        print("Thank you for paying for your ticket, you may now exit the parking garage.")
        self.ticketsav.append(num)
        self.ticketsav = sorted(self.ticketsav)
        self.parkingspace.append(num)
        self.parkingspace = sorted(self.parkingspace)


downtownGarage = Parkinggarage()


def ui():
    while True:
        question = input("Would you like to 'reserve', 'pay' or 'leave'?")
        if question.lower().strip() == "reserve":
            downtownGarage.ticketTaker()
        elif question.lower().strip() == "pay":
            downtownGarage.payingTicket()
        elif question.lower().strip() == "leave":
            downtownGarage.leaving()


ui()
