"""
CTI 110
P3T2 - Choices and Menus
HartyA
9/26/23
"""
# The most simple program, with main ()
def main():
  #Print the menu
  print("-"*10, "Main Menu", "-"*10)
  print("1. Ordering Lunch")
  print("2. Order Beverage")
  print("3. Order Dessert")

  #Let the user choose
  print("Your choice? ", end="")
  choice = int(input())
  print("You chose:", choice)

#branch (if) on choice
  if choice == 1:
    option_1()
  elif choice == 2:
    option_2()
  elif choice == 3:
    option_3()
  else:
    print("Sorry, that's not an option.")
 
def option_1():
   print ("Ordering Lunch")
   print ("Would you like a burger or a salad?")
   food = input()
   if food == "burger":
     print("One burger, coming up")
   elif food == "salad":
     print("Dressing on the side")
   else: 
     print("We don't have any", food)
     
def option_2():
  print("Ordering Beverage")
  print ("Would you like a coffee or fountain drink?")
  beverage = input()
  if beverage == "coffee":
    print("One coffee coming your way")
  elif beverage == "fountain drink":
    print("Mountain Dew it is then")
  else:
    print("We don't have", beverage , "sorry")
    

def option_3():
  print ("Ordering Dessert")
  print ("Options are key lime pie or chocolate lava cake")
  dessert = input()
  if dessert == "key lime pie":
    print("My favorite!")
  elif dessert == "chocolate lava cake":
    print("Thats the house special")
  else:
    print(dessert, "wasn't an option")
 
# start the program
main()

