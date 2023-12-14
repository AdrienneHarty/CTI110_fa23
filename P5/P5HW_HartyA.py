# CTI-110 
# P5HW1 - Math Quiz
# HartyA
# 11/09/23


print("Welcome to Math Quiz")
def main_menu():
    while True:
        print("Main Menu")
        print("1) Adding random numbers")
        print("2) Subtracting random numbers")
        print("3) Exit")
        choice = int(input("Please choose one of the menu options: "))
        
        if choice == 1:
            import random
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            print(f"What is the sum of {num1} and {num2}?")
            answer = int(input("Enter your answer: "))
            guesses = 1
            while answer != num1 + num2:
                if answer < num1 + num2:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")
                answer = int(input("Enter your answer: "))
                guesses += 1
            print(f"Correct! It took {guesses} guesses.")
        elif choice == 2:
            import random
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            print(f"What is the difference between {num1} and {num2}?")
            answer = int(input("Enter your answer: "))
            guesses = 1
            while answer != num1 - num2:
                if answer < num1 - num2:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")
                answer = int(input("Enter your answer: "))
                guesses += 1
            print(f"Correct! It took {guesses} guesses.")
            
        elif choice == 3:
            print("Exiting program")
            break
        else:
            print("Invalid choice. Try again.")

main_menu()
