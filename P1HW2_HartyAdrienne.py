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

budget = float(input("What is your budget?"))
print("Where in the world would you like to visit?")
destination = input()
gas = float(input("How much will you spend on gas?"))
trinkets = float(input("How much will you spend on trinkets?"))
food = float(input("How much will you spend on food?"))
expenses = gas + trinkets + food
amount = budget - expenses
print("Your remaining budget amount is:" + str(amount))