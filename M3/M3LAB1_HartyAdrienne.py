# CTI 110
# M3 LAB1 - Leap Year
# Hartya
# 9/21/23

# Calculate if a year is a leap year
# Leap years are:
# divisible by 4
# unless it's a century, then it's divisibile by 400

#TODO: handle the century case
is_leap_year = False

print("What year to check? ")
year = int(input())

# If the year is divisible by 4, it's a leap year
# We use %, the modulo operator
if year % 4 == 0:
  is_leap_year = True

# Century exception:
# if it's divisible by 100
if year % 100 == 0:
# then it isn't a leap year
  is_leap_year = False
# unless it's ALSO divisbile by 400
if year % 400 == 0:
  #and then it is a leap year
  is_leap_year = True


# output the answer
if is_leap_year:
  print(year, "is a leap year.")
else:
  print(year,"is not a leap year.")
  

