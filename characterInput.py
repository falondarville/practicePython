# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
from datetime import date

print("What is your name?")

name = input()

print("What is your age?")

age = int(input())

current_year = date.today().year

time_from = 100 - age

time_100 = current_year + time_from

print(f"Hi {name}! You turn 100 in the year {time_100}")

