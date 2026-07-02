
# Task
# Load the tips dataset: 
#
# import seaborn as sns
#
# df = sns.load_dataset("tips")
#
# Create ONE figure with TWO charts side by side using plt.subplots(1, 2):
#
# Left chart:
#
# • Bar chart showing the COUNT of bills per day
#
# • Use teal as the bar color
#
# • Title: "Bills per Day"
#
# • Axis labels
#
# Right chart:
#
# • Histogram of total_bill using 15 bins
#
# • Use coral as the color
#
# • Title: "Bill Distribution"
#
# • Axis labels
#
# • Add a main title for the whole figure: "Tips Dataset Overview"
#
# • Use plt.tight_layout() before plt.show()
#
# Your Code:

# Begin your work here

import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")

plt.figure(figsize = (10, 6))

plt.subplot(1, 2, 1)
bills_per_day = df.groupby("day")["total_bill"].count()
plt.bar(bills_per_day.index, bills_per_day.values, color = "teal", ec = "black")
plt.xlabel("Days")
plt.ylabel("Bills")
plt.title("Bills Per Day")

plt.subplot(1, 2, 2)
plt.hist(df["total_bill"], color = "coral", ec = "black", bins = 15)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Bills Distribution")

plt.suptitle("Tips Dataset Overview")
plt.tight_layout()
plt.show()
