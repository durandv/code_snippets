import matplotlib.pyplot as plt
ages = [6, 15, 38, 39, 10, 25, 32, 64, 35, 18, 24, 12, 32, 88]

# Simple hist
#plt.hist(ages)

# With bins
plt.hist(ages, bins=5)

# Show plot
plt.show()

# Clean up
plt.clf()
