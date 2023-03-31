#This project is a pair programming project. This means, that one person(The driver) will code the project while the other people(The navigators)will brainstorm and guide to a working solution.
#Each of you should share/switch these roles every 30mins-1hr (-- Or you may elect to switch "drivers" after creating specific methods of the class).

#The Initial Driver needs to Make sure to:
#create a local folder for the project, create a github repository, commit the inital files, share the link

#Both navigators should then:
#fork the code, clone it and begin.

#The current driver MUST share their screen so the navigators can help brainstorm to a working solution.

#When code has been updated, you will need to pull down the changes.

#Your parking gargage class should have the following methods (SUGGESTIONS):
#- takeTicket
#- This should decrease the amount of tickets available by 1
#- This should decrease the amount of parkingSpaces available by 1
#- payForParking
#- Display an input that waits for an amount from the user and store it in a variable
#- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
#- This should update the "currentTicket" dictionary key "paid" to True
#-leaveGarage
#- If the ticket has been paid, display a message of "Thank You, have a nice day"
#- If the ticket has not been paid, display an input prompt for payment
#- Once paid, display message "Thank you, have a nice day!"
#- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#- Update tickets list to increase by 1 (meaning add to the tickets list)

#You will need a few attributes as well:
#- tickets -> list
#- parkingSpaces -> list
#- currentTicket -> dictionary