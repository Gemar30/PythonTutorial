# # PANDAS- python data analysis library
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #        if row[1] != "temp":
# #            temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# # # print(type(data)) #data type
# # print(type(data["day"]))
#
# # data_dict =  data.to_dict() # converted to dictionary
# # print(data_dict)
#
# # temp_list = data["temp"].to_list() # example of data series converted to become list
# # # average = sum(temp_list) / len(temp_list)
# # # print(average)
# #
# # print(data["temp"].mean()) #average
# # print(data["temp"].max()) #maximum value
# #
# # # Get data in columns
# #
# # print(data["condition"])
# # print(data.condition) #same result
#
# # Get data in row
# print(data[data["day"] == "Monday"])
#
# #maximum temperature
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F= monday_temp * 9/5 + 32
# print(monday_temp_F)
#
#
#
#
# # Create dataframe from scratch
# data_dict =  {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# SQUIRREL COUNT

import pandas as pd

data = pd.read_csv("2018.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict  = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")





