# Assignment# 1
# Task:
# Create a simple list of x values [1,2,3,4,5] and y values [2,4,1,5,3].
# Plot them as a line chart using plt.plot().
# Add a title: "My First Matplotlib Chart".
# Add x-axis label: "X Values" and y-axis label: "Y Values".
# Display the chart using plt.show().
# Begin your work here
import matplotlib.pyplot as plt
import numpy as np

x_values = np.array([1, 2, 3, 4, 5])
y_values = np.array([2, 4, 1, 5, 3])

plt.plot(x_values, y_values)
plt.title("My First Matplotlib Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
