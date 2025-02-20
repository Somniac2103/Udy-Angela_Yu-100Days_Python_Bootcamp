import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# count number of different colours of squirrels and display

condense_data = data["Primary Fur Color"]
gray = 0
cinnamon  = 0
black = 0

for squirrel in condense_data:    
    if (squirrel):
        match squirrel:
            case 'Gray':
                gray += 1
            case 'Cinnamon':
                cinnamon += 1
            case 'Black':
                cinnamon += 1
            case _:
                continue

print(f'Gray = {gray}')
print(f'Cinnamon = {cinnamon}')
print(f'Black = {black}')