import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

tips = pd.read_csv('tips.csv')

print(tips.info())

tips_mean = tips.total_bill.mean()
print("Promedio tips: ",tips_mean)

# Remueve duplicados
tips_noduplicates = tips.drop_duplicates()

# Promedio de tips
tips_mean = tips_noduplicates.total_bill.mean()

print(tips_noduplicates.info())
print("Promedio tips: ",tips_mean)

# print(tips.head())