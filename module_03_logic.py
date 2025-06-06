"""
Description: Introduction to Logic
Author: Kassius Jewar-Tessier
Date: June 2 2025
Usage: To execute, press the play button in the VSC IDE.
"""

# Variables used in this demonstration:
age = 18
sibling_age = 9
horizontal_position = 3
vertical_position = 5
number = 5
fruits = ["apple", "banana", "cherry"]


# CONDITIONALS

# If Statement
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 20:
    print("Young Adult")
else:
    print("Adult")

# NESTED CONDITIONALS
if horizontal_position > 0:
    if vertical_position > 0:
        print("Horizontal and vertical are positive")
    else:
        print("Horizontal is positive, but vertical is not")
else:
    if verticle_position > 0:
        print("Vertical is positive,  but horizontal is not.")
    else:
        print("Both horizontal and vertical are negative.")

# COMPARISON OPERATORS:
first_operand = 5
second_operand = 10
print(first_operand == second_operand) # False
print(first_operand != second_operand) # True
print(first_operand < second_operand) # True
print(first_operand > second_operand) # False
print(first_operand <= second_operand) # True
print(first_operand >= second_operand) # False

# LOGICAL OPERATORS
if age > 0 and sibling_age > 0:
    print("Both values are positive.")
if age > 9 or sibling_age > 9:
    print("At least one value is greater than 9,")
if not age > 10:
    print("Age is not greater than 10.")
    if not sibling_age > 10:
        print("Sibling age is not greater than 10.")

# TERNARY EXPRESSION
# given expression:

# MEMBERSHIP CHECKING
# given expression:
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"
print("result")
# written as a ternary expression:
result = "Even" if number % 2 == 0 else "odd"
print(result)

print("Even" if number % 2 == 0 else "Odd" )

print("banana" in fruits) # True

print("orange" not in fruits) # True

text = "Hello world!"
print("world in text") # True

searched_fruit = "banana"
if searched_fruit in fruits:
    print(f"{searched_fruit} is in the list of fruits.")    
else:
    print(f"{searched_fruit} is not in the list of fruits.")

