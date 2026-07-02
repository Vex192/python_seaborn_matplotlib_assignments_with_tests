
# Assignment #7

# Create a violin plot of total_bill by day:
#
# sns.violinplot(x="day", y="total_bill", data=df)
#
# Then create a boxplot of the same data side by side using subplots.
#
# Compare them: what extra information does the violin plot show that the boxplot does not?
#
# Add titles to both.

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.violinplot(data = df, x = "day", y = "total_bill")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Violin Plot of Total Bill by Day")

plt.subplot(1, 2, 2)
sns.boxplot(data = df, x = "day", y = "total_bill")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Box Plot of Total Bill by Day")

plt.suptitle("Violin Plot vs Box Plot of Total Bill by Day")
plt.tight_layout()
plt.show()
