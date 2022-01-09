import pandas
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = ["Gray", "Cinnamon", "Black"]
color_list = squirrel_data["Primary Fur Color"].to_list()
squirrel_count_dict = {"Fur Color": fur_color, "Count": []}
for color in fur_color:
    squirrel_count_dict["Count"].append(color_list.count(color))
df = pandas.DataFrame(squirrel_count_dict)
df.to_csv("Squirrel Count.csv")