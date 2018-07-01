import pandas as pd

# # Create dictionary my_dict with three key:value pairs: my_dict
# names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
# dr =  [True, False, False, False, True, True, True]
# cpc = [809, 731, 588, 18, 200, 70, 45]
#
# my_dict = {
#     "country": names,
#     "drives_right": dr,
#     "cars_per_cap": cpc
# }

# # Build a DataFrame cars from my_dict: cars
# cars = pd.DataFrame(my_dict)

# # Definition of row_labels
# row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# # Specify row labels of cars
# cars.index = row_labels

# Import from csv
cars = pd.read_csv('cars.csv', index_col=0)

print(cars)

# print(cars[0:3])
# print(cars[3:6])

# # Print out observation for Japan
# print(cars.loc["JAP"])
# print(cars.loc[["AUS","EG"]])

# # Print out drives_right value of Morocco
# print(cars.loc["MOR", "country"])
# print(cars.iloc[5, 0]) # lo mismo que arriba pero con indice

# # Print sub-DataFrame
# print(cars.loc[["RU", "MOR"], ["country", "drives_right"]])
# print(cars.iloc[[4, 5]], [0, 1])

# Print out drives_right column as Series
print(cars.loc[:,"drives_right"])

# Print out drives_right column as DataFrame
print(cars.loc[:,["drives_right"]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ["cars_per_cap","drives_right"]])