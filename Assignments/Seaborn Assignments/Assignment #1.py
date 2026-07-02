
# Assignment #1

# Import seaborn and load the tips dataset.
#
# Run sns.set_theme() to apply the default seaborn style.
#
# Create a simple scatter plot: sns.scatterplot(x="total_bill", y="tip", data=df)
#
# Add a title using plt.title().
#
# Then try sns.set_theme(style="darkgrid") and sns.set_theme(style="whitegrid").
#
# Which style do you prefer?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set_theme(style = "whitegrid")
sns.scatterplot(x = df["total_bill"], y = df["tip"], hue = df["time"])
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend(title = "Time")
plt.title("Scatterplot of Total Bill vs Tip (White Grid Version)")
plt.show()
