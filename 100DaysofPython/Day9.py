# # Dictionaries and Nesting

# #  {"Key": "Value"} - Dictionary syntax
# # programming_dictionary  = {
# #     "Bug": "An error in a program that prevents the program from running as expected.",
# #     "Function": "A piece of code that you can easily call over and over again.",
# #     "Loop": "The action of doing something over and over again."
# # }

# # Retrieving items from dictionary
# #print(programming_dictionary["Function"]) #[key]

# # Adding new items to dictionary.
# # programming_dictionary["While"] = "Types of loop"
# # print(programming_dictionary)

# # Create an empty dictionary
# # empty_dictionary = {}

# # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# # programming_dictionary["Bug"] = "A moth in your computer"
# # print(programming_dictionary)


# # Loop through a dictionary

# # for key in programming_dictionary:
# #     print(key)
# #     print(programming_dictionary[key])

# # GRADING PROGRAM EXERCISE

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }

# # 91 - 100 = "Outstanding", 81 - 90 = "Exceeds Expectations", 71- 80 = "Acceptable", 70 below = Fail

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectation"
#     elif score > 70:
#         student_grades[student]  = "Acceptable"
#     else:
#         student_grades[student]  = "Fail"

# print(student_grades)

# Nesting

# Nesting Dictionary in a list

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5

#     },
# ]

# Dictionary in List Exercises


travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"],
        
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"],
        
},
]
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"]  = times_visited
    new_country["cities"] =  cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Philippines", 5, ["Manila", "Makati"])
print(travel_log)


