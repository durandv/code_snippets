import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

airquality = pd.read_csv('airquality.csv')

print(airquality.info())

# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality.Ozone.fillna(oz_mean)

# Print the info of airquality
print(airquality.info())
