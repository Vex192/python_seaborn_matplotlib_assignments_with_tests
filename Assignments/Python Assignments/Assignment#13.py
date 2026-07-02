
# Assignment #13

# Using the tips dataset:
# 1. Count how many dining bills were recorded each day
# 2. Plot a bar chart showing this count
# 3. Use a different color for each bar
# 4. Add a title, x-label, and y-label
# Which day is the busiest?
# Save or show your chart.

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("tips")
counts_of_bills = df["day"].value_counts()
sns.barplot(counts_of_bills, palette = ["red", "green", "blue", "purple"])
plt.title("Number of Dinner Bills Recorded Each Day")
plt.xlabel("Days")
plt.ylabel("Count")
plt.show()
print("Saturday was the busiest day")
