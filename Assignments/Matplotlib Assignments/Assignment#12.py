
# Assignment# 12

# Load the tips dataset.
# Create one figure with TWO charts side by side:
# Left chart: bar chart of count per day
# Right chart: histogram of total_bill
# Add a title to each chart.
# Add a main title for the whole figure using plt.suptitle().

# Begin your work here

import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")

plt.figure(figsize = (12, 5))

plt.subplot(1, 2, 1)

count = df["day"].value_counts()
plt.bar(count.index, count.values, color="skyblue", ec="black")
plt.title("Count Per Day")

plt.subplot(1, 2, 2)

plt.hist(df["total_bill"], color="skyblue", ec="black")
plt.title("Total Bill Distribution")

plt.suptitle("Tips Data Statistics")
plt.tight_layout()
plt.show()
