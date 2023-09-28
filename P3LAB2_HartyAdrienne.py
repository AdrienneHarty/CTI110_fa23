"""
CTI 110
P3LAB2 - Letter Grades
Hartya
9/28/23

Convert a number grade into a letter grade. (Ten point scale)
"""

print("Enter the number grade: ", end="")
num_grade = int(input())

letter_grade = "G"

if num_grade >= 90:
  letter_grade = "A"
elif num_grade >= 80:
  letter_grade = "B"
elif num_grade >= 70:
  letter_grade = "C"
elif num_grade >= 60:
  letter_grade = "D"
else:
  letter_grade = "F"

#Print the letter grade
print("A grade of", num_grade, "is a", letter_grade)