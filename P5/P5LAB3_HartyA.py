#CTI 110
# P5LAB3 - Quiz Show
# HartyA
# 11/7/23

print("Welcome to the Quiz Show Game!")
print("In this game, you will be asked multiple-choice questions about 1980s metal music.")
print("Choose the correct answer from the options provided.")
print("Let's get started!")
      
questions = [
  {
      "question_text": "What 1980s metal band released the album 'Back in Black'?",
      "choices": {
          "A": "Guns N' Roses" ,
          "B": "Metallica",
          "C": "AC/DC",
          "D": "Def Leppard"
      },
      "answer": "C"
  },
  {
      "question_text": "Which metal band had a hit with the song 'Crazy Train' in the 1980s?",
      "choices": {
          "A": "Ozzy Osbourne",
          "B": "AC/DC",
          "C": "Def Leppard",
          "D": "Guns N' Roses"
      },
      "answer": "A"
  },
  {
      "question_text": "What was the name of the lead singer of the 1980s metal band Guns N' Roses?",
      "choices": {
          "A": "AC/DC",
          "B": "Def Leppard",
          "C": "Ozzy Osbourne",
          "D": "Axl Rose"
      },
      "answer": "D"
  },
  {
      "question_text": "Which metal band released the album 'Master of Puppets' in the 1980s?",
      "choices": {
          "A": "AC/DC",
          "B": "Guns N' Roses",
          "C": "Metallica",
          "D": "Def Leppard"
      },
      "answer": "C"
  },
  {
      "question_text": "What 1980s metal band is known for their song 'Pour Some Sugar on Me'?",
      "choices": {
          "A": "AC/DC",
          "B": "Def Leppard",
          "C": "Guns N' Roses",
          "D": "Metallica"
      },
      "answer": "B"
  }
]
score = 0
for question in questions:
  print(question["question_text"])
  for option, choice in question["choices"].items():
      print(f"{option}: {choice}")
  user_answer = input("Enter your answer (A, B, C, or D): ")
  if user_answer.upper() == question["answer"].upper():
      print("Correct!")
      score += 1
  else:
      print("Incorrect.")
  print()
print("Quiz finished!")
print(f"Your score: {score}/{len(questions)}")