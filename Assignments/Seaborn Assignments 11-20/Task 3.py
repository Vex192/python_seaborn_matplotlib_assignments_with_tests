
# Task 3
# Load the Titanic dataset:
#
# df = sns.load_dataset("titanic")
#
# df["age"].fillna(df["age"].median(), inplace=True)
#
# Write a Python program that:
#
# 1. Creates a FacetGrid using sns.FacetGrid(df, col="pclass")
#
# 2. Uses col_wrap=3 and height=4
#
# 3. Maps sns.histplot onto the grid using "age" as the column to plot, with bins=15
#
# 4. Sets axis labels using g.set_axis_labels("Age", "Count")
#
# 5. Sets titles for each mini-chart using g.set_titles("Class {col_name}")
#
# 6. Shows the chart
#
# This creates THREE small histograms — one for each passenger class.
#
# Write 2 sentences as comments answering:
#
# Which class has passengers spread across the widest age range?
#
# Which class has the youngest average passengers, based on the shape of its histogram?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset("titanic")

md = np.median(df["age"])
df.fillna({md : "age"}, inplace = True)

graph = sns.FacetGrid(df, col="pclass", col_wrap = 3, height = 4)
graph.map(sns.histplot, bins = 15, kde = True, x = df["age"])
graph.set_axis_labels("Age", "Count")
graph.set_titles("Class {col_name}")
plt.suptitle("Passenger Class", y = 1.03)
plt.show()
