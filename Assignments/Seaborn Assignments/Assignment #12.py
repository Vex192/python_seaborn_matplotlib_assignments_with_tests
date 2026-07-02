
# Assignment #12

# Load the tips dataset.
#
# Run: sns.pairplot(df[["total_bill","tip","size"]])
#
# This creates a grid of all combinations automatically.
#
# Then add hue="time" to color by meal time.
#
# Look at the diagonal — what does it show?
#
# Look at total_bill vs tip — what pattern do you see?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.pairplot(df[["total_bill", "tip", "size"]])
sns.pairplot(df[["total_bill", "tip", "size", "time"]], hue = "time")
plt.tight_layout()
plt.show()
