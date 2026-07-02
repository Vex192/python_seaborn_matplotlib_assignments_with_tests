
# Assignment #15

# Make a scatter plot of total_bill (x-axis) vs tip (y-axis).
# Color the dots: green for Dinner, orange for Lunch.
# Add a legend, title, and axis labels.
# Describe the pattern: does a bigger bill mean a bigger tip?
# Is there a group that tips more generously?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.scatterplot(data=df[df["time"]=="Dinner"], x="total_bill", y="tip", color="blue", label="Dinner")
sns.scatterplot(data=df[df["time"]=="Lunch"],  x="total_bill", y="tip", color="orange", label="Lunch")

plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Tip vs Total Bill")
plt.legend(title="Time")
plt.show()
print("A bigger bill means a bigger tip")
