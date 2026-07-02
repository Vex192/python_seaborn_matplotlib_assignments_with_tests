
# Assignment #19

# Using the tips dataset:
# 1. Compute the correlation between total_bill, tip, and size using df[cols].corr()
# 2. Print the result and identify the two most correlated columns
# 3. Plot a heatmap using sns.heatmap with annot=True and cmap="coolwarm"
# 4. In your own words: what does a correlation of 0.6 mean?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
correlation = df[["total_bill", "tip", "size"]].corr()

sns.heatmap(correlation, annot = True, cmap = "coolwarm")
plt.show()

print("A correlation 0.6 means that there is a very good relation between two columns.")
