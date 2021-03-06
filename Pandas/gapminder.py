import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

g1800s = pd.read_csv('gapminder.csv')


# print(g1800s.shape)
# print(g1800s.head(2))
# print(g1800s.info())
# print(g1800s.describe())

# # Create the scatter plot
# g1800s.plot(kind='scatter', x='1800', y='1899')
#
# # Specify axis labels
# plt.xlabel('Life Expectancy by Country in 1800')
# plt.ylabel('Life Expectancy by Country in 1899')
#
# # Specify axis limits
# plt.xlim(20, 55)
# plt.ylim(20, 55)
#
# # Display the plot
# plt.show()

def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()[1:-1]
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0


# # Check whether the first column is 'Life expectancy'
# assert g1800s.columns[0] == 'Life expectancy'
#
# # Check whether the values in the row are valid
# assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()
#
# # Check that there is only one instance of each country
# assert g1800s['Life expectancy'].value_counts()[0] == 1
