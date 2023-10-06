# CTI-110
# P3HW2 - Salary
# HartyA
# 9/30/23
#

employee = str(input("Enter employee's name: "))
hours_worked = float(input("Enter number of hours the employee worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))
overtime = float()
gross_pay = float()
overtime_hours = float()
regular_pay = pay_rate * hours_worked
if (hours_worked > 40):
  overtime_hours = hours_worked - 40
  overtime = (overtime_hours * 1.5) * pay_rate 
  gross_pay = regular_pay + overtime
if (hours_worked < 40):
  gross_pay = regular_pay
print("--------------------")
print()
print("Employee name:", employee)
print()
print("Hours Worked", "\t", "Pay Rate", "\t", "Overtime", "\t", "Overtime Pay", "\t", "Regular Hour Pay", "\t", "Gross Pay" )
print("--------------------------------------------------------------------------------------------")
print(f"{hours_worked:.2f}", "\t\t\t", f"{pay_rate:.2f}", "\t\t", f"{overtime_hours:.2f}", "\t\t", f"{overtime:.2f}", "\t\t", " $", f"{regular_pay:.2f}", "\t\t", " $", f"{gross_pay:.2f}")