
# Assignment# 16

# Plot the store_a line chart from Exercise 9.
# Then improve it:
# Add horizontal grid lines only (axis="y")
# Make grid lines light gray and dashed
# Remove the top and right border lines (spines)
# Compare before and after. Which looks cleaner?

# Begin your work here

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
store_a = np.array([4000, 4200, 3800, 5000, 5500, 6000, 5800, 6200, 6500, 7000, 6800, 7500])

plt.plot(store_a, marker = "o", ls = "-", lw = 2)
plt.grid(axis = "y", color = "lightgray", ls = "--")
plt.xlabel("Months")
plt.ylabel("Sales")
sns.despine()
plt.show()
