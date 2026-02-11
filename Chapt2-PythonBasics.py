# --------------------------------------------
# Name: Jacob Pears
# Date: 02/11/2026
# Program: Chapter 2 Practice
# Description: Pratice questions
# Complete each section by following the
# directions in the comments.
# --------------------------------------------

# ------------------------------------------------
# Practice 1: Variables and print
# ------------------------------------------------
# TODO:
# 1. Create a variable named name
# 2. Store your name as a string in the variable
# 3. Use print() to display: Hello, <name>

name = input("What is your name? ")

print(f"Hello, {name}")  # blank line for readability
print()

# ------------------------------------------------
# Practice 2: Input and output
# ------------------------------------------------
# TODO:
# 1. Ask the user to enter their favorite color
# 2. Store the input in a variable
# 3. Print a sentence that includes the color
fav_color = input("What is your favorite color? ")

print(f"Color is {fav_color}")
print()

# ------------------------------------------------
# Practice 3: Adding two numbers
# ------------------------------------------------
# TODO:
# 1. Ask the user for a number
# 2. Convert the input to an integer
# 3. Ask the user for a second number
# 4. Convert the input to an integer
# 5. Add the two numbers together
# 6. Print the total

first_num = int(input("Pick a number: "))
second_num = int(input("Pick a second number: "))

num_total = first_num + second_num
print(num_total)
print()

# ------------------------------------------------
# Practice 4: Calculations with variables
# ------------------------------------------------
# TODO:
# 1. Ask the user for the price of an item
# 2. Convert the input to a float
# 3. Create a variable for the tax rate (use 0.08)
# 4. Calculate the tax amount
# 5. Calculate the final price
# 6. Print the final price

price = float(input("Price: "))
tax_rate = 0.08

total = price + (price * tax_rate)

print(total)
print()

# ------------------------------------------------
# Practice 5: Formatted output with f-strings
# ------------------------------------------------
# TODO:
# 1. Ask the user how many hours they worked
# 2. Ask the user for their hourly pay
# 3. Convert both inputs to floats
# 4. Calculate weekly pay
# 5. Use an f-string to display the result
#    (Round to 2 decimal places)

hours_worked = float(input("Hours worked: "))
hourly_pay = float(input("Hourly pay: "))
weekly_pay = hours_worked * hourly_pay

print(f"{hours_worked} worked. {hourly_pay} hourly pay. Total Week Pay: {weekly_pay}")
print()