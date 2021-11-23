# example of list comprehension

# numbers = [1, 2, 3]
#
# new_list = [n + 1 for n in numbers]

# name = "Gemar"
#
# new_list = [letter for letter in name]
#
# print(new_list)



# new_range = [n * 2 for n in range(1, 5)]
# print(new_range)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# upper_case_names = [name.upper() for name in names if len(name) > 5]
#
# print(upper_case_names)

# INTER ACTIVE CODING EXERCISE 1
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [n ** 2 for n in numbers]
#
# print(squared_numbers)


# INTER ACTIVE CODING EXERCISE 2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# result = [n for n in numbers if n % 2 == 0]
#
# print(result)

# INTER ACTIVE CODING EXERCISE 3

# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
#
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
#
# result = [int(num) for num in file_1_data if num in file_2_data]

# print(result)
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_score = {student:random.randint(1, 100) for student in names}
#
# passed_students = {student: score for (student, score) in student_score.items() if score >= 60}
# print(passed_students)
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word:len(word) for word in sentence.split()}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
# weather_f = {day:temp_c*9/5 + 32 for (day, temp_c) in weather_c.items()}
#
# # Write your code 👇 below:
#
#
# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas as pd

student_df = pd.DataFrame(student_dict)


#loop through data frame
# for (key, value) in student_df.items():
#     print(key)

for (index, row) in student_df.iterrows():
    print(row.score)