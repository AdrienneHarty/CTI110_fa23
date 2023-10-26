# CTI-110
# P4HW1 - List
# HartyA
# 10/14/23
#

#Ask user to enter for number of scores they would like to enter.
#Create a loop to collect the number of scores the user wants to enter.
#Note every time a score is entered, the following should be done
#Evaluate if the score is valid, it should be between 0 and 100 . 
#If it is not, notify the user and ask for a VALID score to be entered.
#Think of using another loop


#Module1_score = float(input("Enter grade for Module 1 (out of 100):\n "))
#Module2_score = float(input("Enter grade for Module 2 (out of 100):\n "))
#Module3_score = float(input("Enter grade for Module 3 (out of 100):\n "))
#Module4_score = float(input("Enter grade for Module 4 (out of 100):\n "))
#Module5_score = float(input("Enter grade for Module 5 (out of 100):\n "))
#Module6_score = float(input("Enter grade for Module 6 (out of 100):\n "))
#scores = [Module1_score, Module2_score, Module3_score, Module4_score, Module5_score, Module6_score]

#If score is valid. Add the score to a list. Make sure the score list is given an informative name.
#After collecting all the scores. The program is to display the following: 
#Lowest score entered
#Score List after dropping lowest score
#The average of scores in modified list
#Determine the letter grade for the calculated average and display it to user. 

# NOTES AN:
# what variables do we have?
# score_list should be a list
# which score we're on is ... score_num?
# score is the actual test score


score_list = [] # empty list
num_scores = int(input("How many scores do you want to enter? "))
score_num = 0
# we should do range(num_score)
for score_num in range (num_scores):
  print("What is your score for test #", score_num +1, ":", end="")
  score = int(input())
  while score < 0 or score > 100:
      print("Invalid. Score must be between 0 and 100. Enter score: ")
      score = int(input())
  # score is valid, so add it to the list
  score_list.append(score)
  #print("Scores so far:", score_list)
print()
print("------------Results------------")
lowest_score = min(score_list)
print ("Lowest score: \t", f"{lowest_score:.2f}" )
score_list.remove(lowest_score)
print("Modified list: \t", (score_list))
scores_average =sum(score_list)/ len(score_list)
print("Average: \t\t", f"{scores_average:.2f}")
if scores_average >= 90:
  letter_grade = "A"
elif scores_average >= 80:
  letter_grade = "B"
elif scores_average >= 70:
  letter_grade = "C"
elif scores_average >= 60: 
  letter_grade = "D"
else:
  letter_grade = "F"
print("Grade: \t\t\t", letter_grade)
print("--------------------------------------------")