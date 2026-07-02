
# Task 2
# Load the tips dataset.
#
# Write a Python program that:
#
# 1. Creates a histogram of "total_bill" using sns.histplot()
#
# 2. Uses 20 bins and sets kde=True to show the smooth curve
#
# 3. Uses steelblue as the color
#
# 4. Adds title: "Bill Distribution with KDE"
#
# 5. Adds axis labels and shows the chart
#
# Then create a SECOND chart:
#
# 1. Histogram of "tip" column
#
# 2. 15 bins, kde=True, coral color
#
# 3. Title: "Tip Distribution with KDE"
#
# 4. Axis labels and show
#
# Compare the two charts.
#
# Write one comment answering: which column has a more
#
# symmetric distribution — total_bill or tip?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize = (12, 6))

plt.subplot(1, 2, 1)
sns.histplot(df["total_bill"].to_numpy(), bins = 20, kde = True, color = "steelblue")
plt.title("Bill Distribution with KDE")

plt.subplot(1, 2, 2)
sns.histplot(df["tip"].to_numpy(), bins = 20, kde = True, color = "coral")
plt.title("TIp Distribution with KDE")

plt.suptitle("Histograms Of Total Bill and Tip With KDE", y = 0.98, fontsize = 16)
plt.tight_layout()
plt.show()
# Tip is more symmetric because the left skew is not as clean as total bill
