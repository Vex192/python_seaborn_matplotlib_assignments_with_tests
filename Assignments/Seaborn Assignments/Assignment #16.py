
# Assignment #16

# Using the tips dataset, create separate scatter plots (total_bill vs tip) for each day using
#
# FacetGrid:
#
# g = sns.FacetGrid(df, col="day")
#
# g.map(sns.scatterplot, "total_bill", "tip")
#
# This creates one mini-chart per day automatically.
#
# Then try col="time" and row="sex".
#
# When is this better than putting everything on one chart?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

graph = sns.FacetGrid(df, col = "day", col_wrap = 2, height = 4)
graph.map(sns.scatterplot, "total_bill", "tip", alpha = 0.6)
graph.set_axis_labels("Total Bill", "Tip")
graph.set_titles("{col_name}")
plt.show()
