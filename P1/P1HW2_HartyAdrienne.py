#Budget
#09/13/23
#CTI-110 P1HW2 - Travel Expense
#Adrienne Harty
#

#Ask user to enter their budget
#Ask user to enter travel destination
#Ask user for amount they will spend on gas
#Ask user for amount they will spend on accommodation
#Ask user for amount they will spend on food
#Add expenses
#Subtract expenses from budget
#Display results

print("This program calculates and displays travel expenses.")
print()
budget = float(input("Enter Budget:" " "))
print()
destination= str(input("Enter your destination:" " "))
print()
gas = float(input("How much do you think you will spend on gas?" " "))
print()
accomodation = float(input("Approximately, how much will you need for accomodation/hotel?" " "))
print()
food = float(input("Last, how much will you need for food?" " "))
print()
expenses = gas + accomodation + food
amount = budget - expenses
print("Your remaining balance is:" + str(amount))
print()
print("-------------Travel Expenses------------")
print()
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation", accomodation)
print("Food", food)
print()
print("Remaining Balance:", amount)