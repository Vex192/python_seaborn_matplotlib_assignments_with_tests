
# Assignment# 7

# Load the tips dataset from seaborn.
# Plot total_bill (x) vs tip (y) as a scatter chart.
# Color the dots by time: Dinner = steelblue, Lunch = coral.
# Add a legend showing which color is which.
# Write one sentence about what you notice.

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

color1 = df["time"] == "Dinner"
color2 = df["time"] == "Lunch"

plt.scatter(df.loc[color1, "total_bill"], df.loc[color1, "tip"], alpha = 0.6, c = "steelblue", label = "Dinner")
plt.scatter(df.loc[color2, "total_bill"], df.loc[color2, "tip"], alpha = 0.6, c = "coral", label = "Lunch")
plt.legend()
plt.show()
