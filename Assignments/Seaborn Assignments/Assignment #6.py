
# Assignment #6

# Using the tips dataset, create a boxplot:
#
# sns.boxplot(x="day", y="total_bill", data=df)
#
# Then add hue="time" to split each day into Lunch and Dinner boxes.
#
# Identify: Which day has the highest median bill?
#
# Which combination (day + time) has the most outliers?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(data = df, x = "day", y = "total_bill", hue = "time")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Boxplot of Total Bill By Time")

plt.subplot(1, 2, 2)
sns.boxplot(data = df, x = "day", y = "total_bill", hue = "day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Boxplot of Total Bill By Day")
plt.tight_layout()
plt.show()
