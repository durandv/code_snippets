# Import cars data
import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

# # Iterate over rows of cars
# for k, v in cars.iterrows():
#     print("k:" + k)
#     print("v:")
#     print(v)

# # Code for loop that adds COUNTRY column
# for k,v in cars.iterrows():
#     cars.loc[k, "COUNTRY"] = v["country"].upper()

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)