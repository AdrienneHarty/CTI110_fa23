# CTI - 110
# P3HW1 - Letter Grades
# HartyA
# 9/28/23
#
#This program takes a number grade determines average and displays letter grade for average.

Mod_1 = float(input("Enter grade for Module 1 (out of 100):\n "))
Mod_2 = float(input("Enter grade for Module 2 (out of 100):\n "))
Mod_3 = float(input("Enter grade for Module 3 (out of 100):\n "))
Mod_4 = float(input("Enter grade for Module 4 (out of 100):\n "))
Mod_5 = float(input("Enter grade for Module 5 (out of 100):\n "))
Mod_6 = float(input("Enter grade for Module 6 (out of 100):\n "))

grades = [Mod_1, Mod_2, Mod_3, Mod_4, Mod_5, Mod_6]

low = min(grades)
print ("Lowest grade: \t", f"{low:.2f}" )
high = max(grades)
print ("Highest grade: \t", f"{high:.2f}")
sum = sum(grades)
print ("Sum of grades: \t", f"{sum:.2f}")
avg = (Mod_1 + Mod_2 + Mod_3 + Mod_4 + Mod_5 +Mod_6) / 6
print("Average: \t\t", f"{avg:.2f}")

print()
if avg >= 90:
  letter_grade = "A"
elif avg >= 80:
  letter_grade = "B"
elif avg >= 70:
  letter_grade = "C"
elif avg >= 60: 
  letter_grade = "D"
else:
  letter_grade = "F"
print()
print("Your grade is: ", letter_grade)