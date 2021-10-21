# Data Types
# 1. String
# print("Hello"[0])

# 2. Integer
# print(123 + 345)
 
# 3. Floating
# 4. Booleans

# print("Hello"[0])

# CONVERTING INTEGER TO STRING DATA TYPE
# num_char = len(input("What is your Name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters. ")

# a = 123

# print(type(a))

# float()
# str()

# DATA TYPES EXERCISES

# two_digit_number = input("Type a two digit number: ")
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]

# result = int(first_digit) + int(second_digit)
# print(result)

#SAME

# two_digit_number = input("Type a two digit number: ")

# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# BMI exercise

# height = (input("Enter your height in m: "))
# weight = (input("Enter your weight in kg: "))

# # bmi_result = int(weight) / float(height) ** 2

# # print(int(bmi_result)) 

# weight_as_int = int(weight)
# height_as_float = float(height)

# bmi = weight_as_int / height_as_float ** 2

# bmi_as_int = int(bmi)

# print(bmi_as_int)

# ROUNDING NUMBER
# print(round(8 / 3, 2))


# f STRING
# score = 0
# height = 1.8
# isWinning = True

# print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# Life in weeks
age = input("What is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left")




