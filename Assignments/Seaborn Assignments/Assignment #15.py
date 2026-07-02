
# Assignment #15

# Using the tips dataset, create a regression plot:
#
# sns.regplot(x="total_bill", y="tip", data=df)
#
# This adds a line of best fit AND a confidence band automatically.
#
# Does the line go up or down? What does that mean?
#
# Then try: sns.regplot(x="size", y="total_bill", data=df)
#
# Does party size predict the bill?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize = (12, 5))

plt.subplot(1, 2, 1)
sns.regplot(data = df, x = "total_bill", y = "tip", scatter_kws = {"alpha" : 0.4}, line_kws = {"color" : "red"})
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.subplot(1, 2, 2)
sns.regplot(data = df, x = "size", y = "total_bill", scatter_kws = {"alpha" : 0.4}, line_kws = {"color" : "red"})
plt.xlabel("Size")
plt.ylabel("Total Bill")

plt.tight_layout()
plt.show()
