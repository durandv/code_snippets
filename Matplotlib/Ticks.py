import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

# Scatter plot
plt.scatter(year, pop)

# Previous customizations
#plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1900,2000,2100]
tick_lab = ['y1900','y2000','y2100']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

plt.yticks([0, 2, 4, 6, 8, 10],
['0', '2B', '4B', '6B', '8B', '10B'])

# Additional customizations
plt.text(1970, 2, 'AAA')
plt.text(2010, 6, 'BBB')

# Add grid() call
plt.grid(True)

# After customizing, display the plot
plt.show()
