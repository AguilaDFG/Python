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
print(weather_data["temp"])