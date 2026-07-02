
# Assignment #11

# Using the tips dataset:
#
# Create a pivot table of average tip by day and time:
#
# pivot = df.pivot_table(values="tip", index="day", columns="time", 
# aggfunc="mean")
#
# Plot this pivot table as a heatmap.
#
# Which day + time combination has the highest average tip?
#
# Use cmap="YlOrRd" (yellow to red).

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

pivot = df.pivot_table(values = "tip", index = "day", columns = "time", aggfunc = "mean")
sns.heatmap(pivot, annot = True, cmap = "YlOrRd", fmt = ".2f")
plt.show()
