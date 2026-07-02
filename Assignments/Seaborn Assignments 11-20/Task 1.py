
# Task 1
# Load the tips dataset:
#
# import seaborn as sns
#
# import matplotlib.pyplot as plt
#
# df = sns.load_dataset("tips")
#
# Write a Python program that:
#
# 1. Computes the correlation matrix of "total_bill", " tip",and "size" using df[cols].corr()
#
# 2. Plots it as a heatmap using sns.heatmap()
#
# 3. Sets annot=True to show the numbers
#
# 4. Uses cmap="coolwarm"
#
# 5. Uses fmt=".2f" so numbers show 2 decimal places
#
# 6. Adds title: "Correlation Heatmap — Tips Dataset"
#
# 7. Shows the chart
#
# Look at the correlation values.
#
# Write one comment: which two columns are most strongly correlated, and what does that value mean in plain English?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

correlation = df[["total_bill", "tip", "size"]].corr()
sns.heatmap(correlation, annot = True, fmt = ".2f")
plt.title("Correlation Heatmap — Tips Dataset")
plt.show()
# total bill and tip are most correlated that mean that they have strong relation
