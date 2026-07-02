
# Task
# Load the tips dataset.
#
# Write a Python program that:
#
# 1. Creates a regression plot using sns.regplot()
#
# with x="total_bill" and y="tip"
#
# 2. Sets scatter_kws={"alpha":0.4} to make dots transparent
#
# 3. Sets line_kws={"color":"red"} to make the line red
#
# 4. Adds title: "Bill vs Tip — Regression Line"
#
# 5. Adds axis labels and shows the chart
#
# Then create a SECOND regression plot:
#
# 1. x="size" and y="total_bill"
#
# 2. Same styling as above
#
# 3. Title: "Party Size vs Total Bill"
#
# 4. Show the chart
#
# Write one comment for each chart: does the line go up or down, and what does that tell you about the relationship?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize = (12, 5))

plt.subplot(1, 2, 1)
sns.regplot(data = df, x = "total_bill", y = "tip", scatter_kws = {"alpha" : 0.4}, line_kws = {"color" : "red"})
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Bill vs Tip — Regression Line")

plt.subplot(1, 2, 2)
sns.regplot(data = df, x = "size", y = "tip", scatter_kws = {"alpha" : 0.4}, line_kws = {"color" : "red"})
plt.xlabel("Size")
plt.ylabel("Tip")
plt.title("Party Size vs Tip — Regression Line")

plt.tight_layout()
plt.show()
