# Day 3

# Control FLow with if else  and conditional operators
# Conditional statement if else


# Comparison Operator
# > - greater than
# < -  less than
# >= - greater than or equal
# <= - less than or equal
# == - equal to
#!= - not equal to

# SYNTAX
# if condition:
#     do this
# else:
#     do this

# water_level = 50
# if water_level > 80:
#     print("Drain Water")
# else:
#     print("Continue")

# print("Welcome to the RollerCoaster! ")

# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")

# else:
#     print("Sorry, you have to grow taller before you can ride.")


# Comparison Operator
# > - greater than
# < -  less than
# >= - greater than or equal
# <= - less than or equal
# == - equal to
#!= - not equal to

# = - Assigment - assigning value to variables
# == - Check equality - checking if the value on the left is equal to the value of right.


# ODD OR EVEN EXERCISE

# number = int(input("Which number do you want to check? "))


# if number % 2 == 0:
#     print("This is a even number")
# else:
#     print("This is an odd number")

# NESTED IF ELSE STATEMENT

# print("Welcome to the RollerCoaster! ")

# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay 5$.")
#     elif age <= 18:
#         print("Please pay 7$")
#     else:
#         print("Please pay 12$.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# LEAP YEAR EXERCISE

# year = int(input("Which year do you want to check? "))

# # divisible by 4 leap year
# # except every year that is evenly divisble by 100
# # unless the year is also evenly divisble by 400

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#             print("Not a Leap Year")
#     else:
#         print("Leap year!")
# else:
#     print("Not a Leap Year! ")


# print("Welcome to the RollerCoaster! ")

# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the roller coaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are 5$.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are 7$")
#     else:
#         bill = 12
#         print("Adult tickets are 12$")
    
#     wants_photo = input("Do you want a photo taken? Y or N.")
#     if wants_photo == "Y" or wants_photo == "y":
#         # Add 3$ to their bill
#         bill += 3

#     print(f"Your final bill is {bill}")

# else:
#     print("Sorry you chave to grow taller before you can ride.")


# Pizza Order practice
# Small = $15
# Medium = $20
# Large = $25

# Pepperoni for small pizza + 2$
# Pepperono for medium or large pizza: + 3$

# #Extra Cheese for any pizza + 1$
# print("Welcome to Python Pizza Deliveries!")

# size = input("What size of pizza do you want? S, M, L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# price = 0

# if size == "S":
#     price += 15
# elif size == "M":
#     price += 20
# elif size == "L":
#     price += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         price += 2
#     else:
#         price +=3

# if extra_cheese == "Y":
#     price += 1

# print(f"Your final bill is: ${price}")

# LOVE CALCULATOR EXERCISE

from ast import unparse


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1+name2
lower_case_string = combined_string.lower()

t =lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l =lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))


# < 10 or > 90
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos. ")
# between 40 and 50
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together. ")
else:
    print(f"Your score is {love_score}")
    







