# CTI-110
# P2HW2 - List
# HartyA
# 9/21/23
#
#Asks the user to enter grades for following tests. 
#Each grade is to be requested in a separate statement. 

Module1_grade = float(input("Enter grade for Module 1 (out of 100):\n "))
Module2_grade = float(input("Enter grade for Module 2 (out of 100):\n "))
Module3_grade = float(input("Enter grade for Module 3 (out of 100):\n "))
Module4_grade = float(input("Enter grade for Module 4 (out of 100):\n "))
Module5_grade = float(input("Enter grade for Module 5 (out of 100):\n "))
Module6_grade = float(input("Enter grade for Module 6 (out of 100):\n "))

grades = [Module1_grade, Module2_grade, Module3_grade, Module4_grade, Module5_grade, Module6_grade]

print("------------Results------------")
lowest_grade = min(grades)
print ("Lowest grade: \t", f"{lowest_grade:.2f}" )
highest_grade = max(grades)
print("Highest grade: \t", f"{highest_grade:.2f}")
sum_of_grade = (Module1_grade + Module2_grade + Module3_grade + Module4_grade + Module5_grade + Module6_grade)
print("Sum of grades: \t", f"{sum_of_grade:.2f}")
average = (Module1_grade + Module2_grade + Module3_grade + Module4_grade + Module5_grade + Module6_grade) / 6
print("Average: \t\t", f"{average:.2f}")
print("--------------------------------------------")