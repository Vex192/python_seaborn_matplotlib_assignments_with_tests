
# Assignment #2

# Using the tips dataset, create a scatter plot of total_bill vs tip.
#
# Set hue="time" so Lunch and Dinner get different colors automatically.
#
# Then try hue="sex" and hue="day".
#
# Seaborn handles the legend automatically — notice how little code this needs vs Matplotlib.

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize = (15, 5))

plt.subplot(1, 3, 1)
sns.scatterplot(x = df["total_bill"], y = df["tip"], hue = df["time"])
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend(title = "Time")
plt.title("Total Bill vs Tip By Time")

plt.subplot(1, 3, 2)
sns.scatterplot(x = df["total_bill"], y = df["tip"], hue = df["sex"])
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend(title = "Sex")
plt.title("Total Bill vs Tip By Sex")

plt.subplot(1, 3, 3)
sns.scatterplot(x = df["total_bill"], y = df["tip"], hue = df["day"])
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend(title = "Day")
plt.title("Total Bill vs Tip By Day")

plt.suptitle("Total Bill vs Tip By Various Filters")
plt.tight_layout()
plt.show()
