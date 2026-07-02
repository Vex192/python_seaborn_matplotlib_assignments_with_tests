
# Assignment #13

# Using the tips dataset, plot average total_bill by day:
#
# sns.lineplot(x="day", y="total_bill", data=df)
#
# Seaborn automatically draws the mean AND a shaded confidence band.
#
# Then add hue="time" to get separate lines for Lunch and Dinner.
#
# What does the shaded area around each line represent?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize = (12, 6))

plt.subplot(1, 2, 1)
sns.lineplot(data = df, x = "day", y = "total_bill")
plt.xlabel("Days")
plt.ylabel("Total Bill")
plt.title("Average Bill By Day With Confidence Interval")

plt.subplot(1, 2, 2)
sns.lineplot(data = df, x = "day", y = "total_bill", hue = "time")
plt.xlabel("Days")
plt.ylabel("Total Bill")
plt.title("Average Bill By Day And Time With Confidence Interval")

plt.tight_layout()
plt.show()
