# Adding on to P1HW2
# 09/16/2023
# CTI-110 P2HW1 - Travel
# Adrienne Harty
#
print("This program calculates and displays travel expenses.")
print()
budget = float(input("Enter budget:" " "))
print()
destination = str(input("Enter destination:" " "))
print()
gas = float(input("How much do you think you will spend on gas?" " "))
print()
accomodation = float(input("Approximately, how much will you need for accomodation/hotel?" " "))
print()
food = float(input("Last, how much do you need for food?" " "))
print()
expenses = gas + accomodation + food
amount = budget - expenses
print("Your remaining balance is:" + str(amount))
print()
print("------------Travel Expenses-------------")
print()
print("Location:\t\t",destination)
print()
print("Initial Budget:" "\t\t", "$", budget)
print()
print("Fuel:", "\t\t\t\t", "$", gas)
print()
print("Accomodations:", "\t\t", "$",accomodation)
print("Food:", "\t\t\t\t", "$", food)
print()
print("----------------------------------------")
print()
print("Remaining Balance:", "\t", amount)