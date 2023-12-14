"""
CTI 110
M5LAB2 - Complete a Program
Abdiel Ortiz & Adrienne Harty
11/9/23

The program will ask the user to enter the width and length of a rectangle. It will then calculate the area. Finally it will display all three values in well formatted output.

The program will contain the following functions as well as main().

getLength - Asks the user to enter a rectangle's length, and return that value as a float.

getWidth - Asks the user to enter a rectangle's width, and return that value as a float.

getArea - This function should take two arguments, length and width. It will calculate the area and return that value as a float.

displayData - This function should take three arguments, length, width, and area. It will then display these values as well formatted output. (Something like "The length is: 5".)
"""

def getLength():
    """
    Ask the user to enter the rectangle's length, and return that value as a float.
    """
    length = float(input("What is the length? "))
    return length

def getWidth():
    """
    Ask the user to enter the rectangle's width, and return that value as a float.
    """
    width = float(input("What is the width? "))
    return width
def getArea(length, width):
    """
    Calculate the area using the provided length and width, and return that value as a float.
    """
    print("What is the area?")
    
    area = length * width
    return area

def displayData(length, width, area):
    """
    Display the length, width, and area values.
    """
    print("The length is: " , length, "The width is: ", width, "The area is: ", area)
          

def main():
  
    length = getLength()
    print (length)
    width = getWidth()
    print (width)
    area = getArea(length, width)
    displayData(length, width, area)

# start the program
main()
