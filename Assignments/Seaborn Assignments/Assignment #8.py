
# Assignment #8

# Using the tips dataset, create a histogram of total_bill:
#
# sns.histplot(df["total_bill"], bins=20, kde=True)
#
# The kde=True adds a smooth curve showing the distribution shape.
#
# Then try kde=True on the "tip" column.
#
# What does the KDE curve tell you that the bars alone do not?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(data = df, x = "total_bill", bins = 20, kde = True)
plt.title("Histogram of Total Bill with KDE")

plt.subplot(1, 2, 2)
sns.histplot(data = df, x = "tip", bins = 20, kde = True)
plt.title("Histogram of Tip with KDE")

plt.tight_layout()
plt.suptitle("Histograms with KDE")
plt.show()
