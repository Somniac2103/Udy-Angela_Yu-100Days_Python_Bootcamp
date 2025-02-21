import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# count number of different colours of squirrels and display

# ----My version -----

# condense_data = data["Primary Fur Color"]
# gray = 0
# cinnamon  = 0
# black = 0

# for squirrel in condense_data:    
#     if (squirrel):
#         match squirrel:
#             case 'Gray':
#                 gray += 1
#             case 'Cinnamon':
#                 cinnamon += 1
#             case 'Black':
#                 black += 1
#             case _:
#                 continue

# print(f'Gray = {gray}')
# print(f'Cinnamon = {cinnamon}')
# print(f'Black = {black}')

# ---- Angela Version -----

grey_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")