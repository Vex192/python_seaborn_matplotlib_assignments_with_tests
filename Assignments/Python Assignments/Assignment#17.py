
# Assignment #17

# Using the tips dataset, create a boxplot of total_bill grouped by day of week.
# Use seaborn: sns.boxplot(x="day", y="total_bill", data=df)
# Add a title.
# Answer these questions in comments in your code:
# Which day has the widest spread?
# Can you see dots above or below the whiskers? Those are outliers!
# What does the line inside the box represent?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.boxplot(x = "day", y = "total_bill", data=df)
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Total Bill Per Day")
plt.show()
print("Saturday has the widest spread.")
print("There are dots above and below the whiskers these are extreme values or outliers and are different from the data near the mean.")
print("The line inside the box represents the median.")
