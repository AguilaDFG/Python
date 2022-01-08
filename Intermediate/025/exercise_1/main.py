#with open("weather_data.csv") as data:
#    weather_data = data.readlines()
#    print(weather_data)

#import csv
#with open("weather_data.csv") as data:
#    weather_data = csv.reader(data)
#    temperatures = []
#    for row in weather_data:
#        if row != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas
weather_data = pandas.read_csv("weather_data.csv")
#print(weather_data["temp"])

#weather_dict = weather_data.to_dict()
#print(weather_dict)
#temp_list = weather_data["temp"].to_list()
#print(temp_list)

#temp_average = sum(temp_list) / len(temp_list)
#print(temp_average)
#print(weather_data["temp"].mean())
#print(weather_data["temp"].max())

#print(weather_data[weather_data.day == "Monday"])
#print(weather_data[weather_data.temp == weather_data.temp.max()])

#monday = weather_data[weather_data.day == "Monday"]
#monday_temp_F = monday.temp*9/5 + 32
#print(monday_temp_F)
