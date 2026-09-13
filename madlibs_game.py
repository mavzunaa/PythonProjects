# Mad Libs is a word game where you create a funny story by filling in missing words.

# So the main idea of Mad Libs is extremely simple:
# Ask the user for words → store those words → put those words into a story.
# This is actually a great input() exercise for practicing exactly what you've been learning.

# Practice #1
# example of output: The scary dog was running.

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb ending with 'ing': ")

print(f"The {adjective} {noun} was {verb}")

# Practice #2
# example of output:
# Today I saw a funny dog.
# The dog was crazy and running!

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb ending with 'ing': ")

print(f"Today I saw a {adjective} {noun}.")
print(f"The {noun} was {adjective} and {verb}!")

# Practice #3
# example output:
# Alex was walking through a strange supermarket.
# Suddenly, a penguin appeared.
# The penguin was dancing on the table.
# Alex ran away screaming.

name = input("Enter a person's name: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")
verb = input("Enter a verb ending with 'ing': ")

print(f"{name} was {verb} through a {adjective} {place}.")
print(f"Suddenly, a {animal} appeared.")
print(f"The {animal} was {verb} on the {place}.")
print(f"{name} ran away {verb}.")

# Practice #4
# example output:
# Hello Alex!
# You are 25 years old.
# Your height is 1.80 meters.
#
name = input("Enter a person's name: ")
age = int(input("Enter age: "))
height = float(input("Enter a height: "))

print(f"Hello {name}!")
print(f"You are {age} years old.")
print(f"Your height is {height} meters.")

# Practice #5
# This part of practice should be improved.

# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("That's not a valid number.")