
# Assignment# 13

# Load the tips dataset.
# Create a 2x2 subplot grid showing:
# Top-left: bar chart of bills per day
# Top-right: histogram of total_bill
# Bottom-left: scatter of total_bill vs tip
# Bottom-right: bar chart of average tip per day
# Use plt.tight_layout() to prevent overlap.

# Begin your work here

import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")

plt.figure(figsize=(12,6))

plt.subplot(2, 2, 1)
count = df["day"].value_counts()
plt.bar(count.index, count.values, color="skyblue", ec = "black")
plt.title("Bills Per Day")

plt.subplot(2, 2, 2)
plt.hist(df["total_bill"], color="skyblue", ec = "black")
plt.title("Total Bill Distribution")

plt.subplot(2, 2, 3)
plt.scatter(df["total_bill"], df["tip"], color="skyblue", alpha = 0.6, ec = "black")
plt.title("Total Bill vs. Tip Comparison")

plt.subplot(2, 2, 4)
mn_tip = df.groupby("day")["tip"].mean()
plt.bar(mn_tip.index, mn_tip.values, color="skyblue", ec="black")
plt.title("Average Tip Per Day")

plt.suptitle("Tips Dataset Overview")
plt.tight_layout()
plt.show()
