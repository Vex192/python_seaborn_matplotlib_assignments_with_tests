
# Assignment# 18

# You have monthly sales (dollars) and temperature (Celsius) data for 12 months.
# Sales: [9000,8500,11000,13000,12500,15000,14000,16000,17500,15000,13000,18000]
# Temperature: [5, 7, 12, 18, 22, 28, 32, 31, 25, 18, 10, 6]
# Plot sales as a bar chart on the left y-axis.
# Plot temperature as a line on the right y-axis using ax.twinx().
# Label both y-axes.

# Begin your work here

import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "Sales": [9000, 8500, 11000, 13000, 12500, 15000, 14000, 16000, 17500, 15000, 13000, 18000],
    "Temperature": [5, 7, 12, 18, 22, 28, 32, 31, 25, 18, 10, 6]
})

df["Sales"].plot(kind = "bar", color = "steelblue", ylabel = "Sales")
df["Temperature"].plot(secondary_y = True, color = "red", marker = "o", ylabel = "Sales")
plt.show()
# Work Smart Not Hard ax.twinx = No, Use Pandas and work smart = Yes
