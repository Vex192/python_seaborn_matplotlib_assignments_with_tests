
# Assignment #4

# Load the tips dataset.
#
# Create a bar chart: sns.barplot(x="day", y="total_bill", data=df)
#
# Seaborn automatically shows the mean AND a confidence interval (the error bar on top).
#
# What does the error bar represent?
#
# Then try x="time" and x="sex".

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.barplot(data = df, x = "day", y = "total_bill")
plt.xlabel("Days")
plt.ylabel("Total Bill")
plt.title("Average Total Bill by Day")
plt.show()
