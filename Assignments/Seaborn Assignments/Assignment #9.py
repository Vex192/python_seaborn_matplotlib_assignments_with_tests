
# Assignment #9

# Using the tips dataset, plot two KDE curves on the same chart:
#
# One for Dinner total_bill
#
# One for Lunch total_bill
#
# Use fill=True to shade under each curve.
#
# Set alpha=0.4 so the curves overlap clearly.
#
# Which meal tends to have higher bills?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(12, 6))


sns.histplot(data = df, x = "total_bill", bins = 20, kde = True, hue = "time", fill = True, alpha = 0.4)
plt.xlabel("Total Bill")
plt.title("Histogram of Total Bill with KDE")
plt.show()
