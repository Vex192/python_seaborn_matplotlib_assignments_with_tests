
# Assignment #18

# Load the Titanic dataset.
#
# Create a pivot table showing survival RATE by sex and passenger class:
#
# pivot = df.pivot_table(values="survived", index="sex", columns="pclass", aggfunc="mean")
#
# Plot as a heatmap with annot=True and fmt=".0%" to show percentages.
# Write 2 sentences about what you find.

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

pivot = df.pivot_table(values = "survived", index = "sex", columns = "pclass", aggfunc = "mean")
sns.heatmap(pivot, annot = True, fmt = ".0%", cmap = "coolwarm")
plt.show()
