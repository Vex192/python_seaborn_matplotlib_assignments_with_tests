
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
# 1. Creates a Seaborn bar chart of "day" vs "total_bill" using sns.barplot()
#
# 2. Uses the "Set2" color palette
#
# 3. Adds title: "Average Bill by Day with Confidence Interval"
#
# 4. Adds axis labels for x and y
#
# 5. Shows the chart
#
# Then create a SECOND chart — same bar chart but use x="time
# " instead of x="day".
#
# Add title: "Average Bill by Meal Time"
#
# Show the chart.
#
# Look at the error bars on both charts.
#
# Write one comment: which group has the widest error bar and why
#
# that might be the case.

# Begin your work here

import seaborn as sns

import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize = (13, 6))

plt.subplot(1, 2, 1)
sns.barplot(data = df, x = "day", y = "total_bill", palette = "Set2")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Average Bill by Day with Confidence Interval")

plt.subplot(1, 2, 2)
sns.barplot(data = df, x = "time", y = "total_bill", palette = "Set2")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Average Bill by Mealtime with Confidence Interval")

plt.suptitle("Average Bill By Various X Values With Confidence Interval", y = 1.03)
plt.tight_layout()
plt.show()
