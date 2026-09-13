# User Input:
# The process of receiving data from a user
# and making that data available to the program
# for further processing.

# input() always returns a string (str), even if the user enters a number.

name = input("What is your name? ")
age = int(input("How old are you? "))
# score = int(input("What is your score? "))

print(f"Hello, {name}!")
print(f"You are {age} years old.")
# if score >= 90:
#     print("Excellent")
# elif score >= 75:
#     print("Good")
# elif score >= 50:
#     print("Pass")
# else:
#     print("Fail")

# Ex: Rectangular Area calc
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length  * width

# The easiest way to print are:
# print(area)
print(f"The area is: {area}cm²")

# Ex: Shopping Cart Program
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")





