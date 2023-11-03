# CTI-110
# P4HW2 - Salary Calculator
# HartyA
# 10/14/23
#
#For assignment P4HW2, you will build on P3HW2 assignment. The program however will calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

#Asks the user employee name
#Enter user pay rate and hours worked
#Calculate overpay and regular pay. Store these values in variables, at the end of the program you will display overtime total, regular pay total, gross pay total, and number of employees entered
#Ask user to enter another employee's name to calculate salary for or "Done" to terminate program. Note we are using sentinels here.
#When user chooses to stop entering employee information , display results as shown in image below.
#THE PROGRAM ONLY TERMINATES IF THE USER ENTERS "Done" for employee name.

count = 0
total_overtime = 0
total_reg_hours = 0
total_gross = 0
name = str(input("Enter employee's name or 'Done' to terminate: "))
while name != "Done": 
  hours_worked = float(input("How many hours did "+ name + " work? "))
  pay_rate = float(input("What is " + name + " pay rate: "))
  overtime= float()
  gross_pay = float()
  overtime_hours = float()
  regular_pay = pay_rate * hours_worked
  count += 1
  
  if (hours_worked > 40):
        overtime_hours = hours_worked - 40
        overtime = (overtime_hours * 1.5) * pay_rate 
        gross_pay = regular_pay + overtime
  else:
    overtime = 0
    gross_pay = regular_pay
  total_overtime += overtime
  total_reg_hours += regular_pay
  total_gross += gross_pay
  print("--------------------")
  print()
  print("Employee name:", name)
  print()
  print("Hours Worked", "\t", "Pay Rate", "\t", "Overtime", "\t",         "Overtime Pay", "\t", "Regular Hour Pay", "\t", "Gross Pay" )
  print("--------------------------------------------------------------------------------------------")
  print(f"{hours_worked:.2f}", "\t\t\t", f"{pay_rate:.2f}",               "\t\t", f"{overtime_hours:.2f}", "\t\t", f"{overtime:.2f}",             "\t\t", " $", f"{regular_pay:.2f}", "\t\t", " $", f"                     {gross_pay:.2f}")
  name = str(input("Enter employee's name or 'Done' to terminate: ")) 


  
  """
  print("--------------------")
  print()
  print("Employee name:", name)
  print()
  print("Hours Worked", "\t", "Pay Rate", "\t", "Overtime", "\t",       "Overtime Pay", "\t", "Regular Hour Pay", "\t", "Gross Pay" )
  print("--------------------------------------------------------------------------------------------")
  print(f"{hours_worked:.2f}", "\t\t\t", f"{pay_rate:.2f}", "\t\t", f"{overtime_hours:.2f}", "\t\t", f"{overtime:.2f}", "\t\t", " $", f"{regular_pay:.2f}", "\t\t", " $", f"{gross_pay:.2f}")
"""
print(f'Total number of employees entered:  {count:<10}')
print(f'Total amount paid for overtime: {total_overtime:.2f}  ')
print(f'Total amount paid for regular hours:  {total_reg_hours:.2f} ')
print(f'Total amount paid in gross: {total_gross:.2f} ')