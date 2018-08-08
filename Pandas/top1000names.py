import numpy as np
import matplotlib.pyplot as pp
import pandas as pd
import seaborn sb
import zipfile
import os


# https://www.digitalocean.com/community/tutorials/data-analysis-and-visualization-with-pandas-and-jupyter-notebook-in-python-3

# print(pp.style.available)
pp.style.use('seaborn-white')

def name_plot(sex, name):
    data = all_names_index.loc[sex, name]
    pp.plot(data.index, data.values)


# Extracts files if directory not exist
if (not os.path.isdir('top1000names')):
    zipfile.ZipFile('top1000names.zip').extractall('./top1000names')

all_years = []
for year in range(1880, 2018):
    all_years.append(pd.read_csv('./top1000names/yob{}.txt'.format(year), names=['Name', 'Sex', 'Babies']))
    all_years[-1]['Year'] = year
    print(year)

all_names = pd.concat(all_years)
# print(all_names.tail())

# Group
group_name = all_names.groupby(['Sex', 'Year'])
# print(group_name.size().unstack())

# Pivot
pv = pd.pivot_table(all_names, 'Babies', ['Name', 'Sex'], 'Year')
# print(pv)

# Visualization
all_names_index = all_names.set_index(['Sex', 'Name', 'Year']).sort_index()
# print(all_names_index.loc['M', 'Aaron'])

pp.figure(figsize=(18, 8))
names = ['Sammy', 'Jesse', 'Emma', 'Jamie', 'Ada']
for name in names:
    name_plot('F', name)
pp.legend(names)
pp.show()

sns.distplot();