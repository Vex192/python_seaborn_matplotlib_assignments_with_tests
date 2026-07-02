
# Assignment #16

# Create a list of monthly sales for 12 months — invent realistic numbers between 8000 and 20000.
# Plot a line chart with a circular marker at each data point.
# Label the x-axis with month names (Jan through Dec).
# Use teal as the line color.
# Give it a title and y-axis label.

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sales = np.array([8090, 7000, 6500, 10000, 9000, 7500, 8900, 9500, 6800, 11000, 10500, 8800])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sns.lineplot(x = months, y = sales, c = "teal")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales For a Year")
plt.show
