# with open("./weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv

# with open("./weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# temp_ave = data["temp"].mean()
# print(int(round(temp_ave,0)))

# print(int(round(data["temp"].max(),0)))

# print(data["condition"])
# print(data.condition)

# get data in row

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# print(((data[data.day == "Monday"].temp)*9/5)+32)

# create a dataframe afrom scratch
data_dict = {
    "students" : [ "Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)





