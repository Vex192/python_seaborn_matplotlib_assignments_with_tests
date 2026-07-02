
# Assignment #14

# Plot a histogram of total_bill from the tips dataset using 15 bins.
# Add a vertical red dashed line at the mean value.
# Label that line using the legend.
# Is the distribution symmetric, or does it lean to one side?
# Write one sentence describing the shape.

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset("tips")
mn = np.mean(df["total_bill"])
total_bill = df["total_bill"]
sns.histplot(total_bill, bins = 15)
plt.axvline(mn, c = "red", ls = "--", label = "Mean of Total Bill")
plt.legend()
plt.show()
skew = df["total_bill"].skew()
if skew >= 1:
    print("The data is skewed right")
elif skew == 0:
    print("The data is symmetric")
elif skew <= -1:
    print("The data is skewed right.")
