# Function with inputs
# Arguments and Parameters


# def my_function()
# call the function: my_function()

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()

# Function that allows for input
# Parameter - name of the data that being passed on.
# Argument - actual value of the data

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")

# greet_with_name("Gemar")


# Function with more than one input

# def greet_with(name, location):
#     print(f"Hello {name}.")
#     print(f"What is it like in {location}.")

# greet_with(name = "Gemar", location = "Makati")

# Paint area calculator Exercise

# import math


# def paint_calc(height, width, cover):
#     num_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {num_of_cans} cans of paint")

# #number of cans = (wall height * wall width) / coverage per can

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# paint_calc(height= test_h, width=  test_w, cover = coverage)

# PRIME NUMBER CHECKER

# def prime_checker(number):
#     is_prime = True

#     for i in range(2, number - 1):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")

# n = int(input("Check this number: "))

# prime_checker(number=n)








