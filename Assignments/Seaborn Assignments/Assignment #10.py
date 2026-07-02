
# Assignment #10

# Load the tips dataset.
#
# Compute the correlation matrix: df[["total_bill","tip","size"]].corr()
#
# Plot it as a heatmap using sns.heatmap().
#
# Use annot=True to show numbers, cmap="coolwarm" for colors.
#
# Which two columns are most correlated?
#
# What does a value of 0.67 mean in plain English?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

correlation = df[["total_bill", "tip", "size"]].corr()
sns.heatmap(correlation, annot = True, cmap = "coolwarm")
plt.title("Correlation Heatmap")
plt.show()
