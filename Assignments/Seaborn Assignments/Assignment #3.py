
# Assignment #3

# Using the tips dataset:
#
# Create a scatter plot with:
#
# hue="time" (color by meal time)
#
# size="size" (dot size = party size)
#
# style="sex" (shape of dot = male/female)
#
# This one chart shows 5 variables at once.
#
# Write one sentence: what pattern do you notice?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize = (12, 6))

sns.scatterplot(data  = df, x = "total_bill", y = "tip", hue = "time", size = "size", style = "sex")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend()
plt.title("Total Bill vs Tip 5 Variables")
plt.show()
