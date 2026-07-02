
# Assignment #14

# Using the tips dataset, create two charts side by side:
#
# Left: sns.stripplot(x="day", y="total_bill", data=df)
#
# Right: sns.swarmplot(x="day", y="total_bill",ot; data=df)
#
# What is the difference between them?
#
# Which one avoids dot overlap?
#
# When would you use each one?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize = (12, 6))

plt.subplot(1, 2, 1)
sns.stripplot(data = df, x = "day", y = "total_bill")
plt.xlabel("Days")
plt.ylabel("Total Bill")

plt.subplot(1, 2, 2)
sns.swarmplot(data = df, x = "day", y = "total_bill")
plt.xlabel("Days")
plt.ylabel("Total Bill")

plt.tight_layout()
plt.show()
# Strip is less wide while swarm is more wide stripplot doesnt avoid overlap while swarm does
