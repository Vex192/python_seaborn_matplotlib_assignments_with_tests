
# Assignment #17

# sns.catplot() is a universal function — change the kind parameter to switch chart types.
#
# Using tips dataset, try all of these:
#
# kind="bar" → mean with CI
#
# kind="box" → boxplot
#
# kind="violin" → violin
#
# kind="strip" → raw dots
#
# Use x="day", y="total_bill" for each.
#
# Which kind gives the most information?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.catplot(data = df, kind = "bar", x = "day", y = "total_bill")
plt.title("Catplot With Kind As Bar")

sns.catplot(data = df, kind = "box", x = "day", y = "total_bill")
plt.title("Catplot With Kind As Box")

sns.catplot(data = df, kind = "violin", x = "day", y = "total_bill")
plt.title("Catplot With Kind As Violin")

sns.catplot(data = df, kind = "strip", x = "day", y = "total_bill")
plt.title("Catplot With Kind As Strip")

plt.show()
