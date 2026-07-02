
# Assignment# 10

# Plot store_a data from Exercise 9 as a line chart.
# Find the month with the highest value.
# Add an annotation arrow pointing to that peak with the text "Best Month".
# Also add a text label at the lowest point saying "Slow Month".
# Annotations help guide the viewer to important findings.

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
store_a = np.array([4000, 4200, 3800, 5000, 5500, 6000, 5800, 6200, 6500, 7000, 6800, 7500])

plt.plot(months, store_a, marker = "o", lw = 2)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Store A Sales Per Month")
plt.annotate("Best Month", (12, 7500), (8, 7530), arrowprops = {"arrowstyle": "->"})
plt.annotate("Slow Month", (1, 4000), (4, 4000), arrowprops = {"arrowstyle": "->"})
plt.show()
