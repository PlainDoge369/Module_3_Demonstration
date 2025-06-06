"""
Description: Introduction to Loops
Author: Kassius Jewar-Tessier
Date: June 2 2025
Usage: To execute, press the play button in the VSC IDE.
"""

# Variables used in this demonstration:
fruits = ["apple", "orange", "banana", "cherry"]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# FOR LOOP
for fruit in fruits:
    print(fruit)
for i in range(10): # 0 -> 9
    print(i)
for i in range(2, 8): # 2 -> 7
    print(i)
for i in range(1, 10, 2): # 1 -> 9 by 2
    print(i)
for i in range(-10, 0): # -10 -> 0
    print(i)

# INPUT FUNCTION
name = input("Enter your name: ")
while True:
    try:
        salary = float(input("What is your current salary "))
        break
    except ValueError:
        print("Error: Please enter a valid number for the salary.")
print(f"Name: {name} \nSalary: ${salary:,.2f}")

# WHILE LOOP
favorite_number = 0
while favorite_number < 100:
    try:
        favorite_number = int(input("Enter your favorite number (but not 7!), 100 & up to quit: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        continue
    if favorite_number == 7:
        print("You broke this game!")
        break
    elif favorite_number < 100:
        print("Your favorite number is too small!")
    else:
        print("Your favorite number is too big!")

# LOOP CONTROL STATEMENTS
# CONTINUE
# Use a for loop to iterate over the range of integers from 1 to 9 (exclusive).
for number in range(1, 10):
    # Use continue statement to skip over multiples of 3.
    if number % 3 == 0:
        continue
    # Print all other integers
    print(number)
# Output: 1, 2, 4, 5, 7, 8

# CONTINUE:
for number in range(1, 10):
    if number % 3 == 0:
        continue
    print(number)

# BREAK:
for number in range(1, 10):
    if number > 5:
        break
    print(number)
# Infinte loop
number = 10
while number > 0:
    number += 1
print(number)
# How could we avoid this?
# to prevent the infinite
loop
number = 10
while number > 0:
    if number > 100:
        break
    number += 1
print(number)


# NESTED LOOP
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # Newline after each row