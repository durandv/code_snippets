# Import cars data
import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)
# print(cars)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
# print(sel)

cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)
