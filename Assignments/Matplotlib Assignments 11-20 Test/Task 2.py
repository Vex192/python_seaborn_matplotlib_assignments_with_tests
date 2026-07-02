
# Task
# Use this data:
#
# months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# sales = [9000, 8500, 11000, 13000, 12500, 15000, 14000, 16000, 17500, 15000, 13000, 18000]
#
# Write a Python program that:
#
# 1. Creates the chart using fig, ax = plt.subplots()
# 2. Plots sales as a teal line with circle markers
# 3. Adds horizontal grid lines ONLY (axis="y")
# 4. Makes grid lines light gray and dashed
# 5. Removes the TOP and RIGHT border lines (spines)
# 6. Adds title: "Monthly Sales — Clean Style"
# 7. Adds axis labels and shows the chart
#
# Write one comment explaining why removing spines makes a chart look better.
# Your Code:

# Begin your work here

import matplotlib.pyplot as plt
import seaborn as sns

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

sales = [9000, 8500, 11000, 13000, 12500, 15000, 14000, 16000, 17500, 15000, 13000, 18000]

plt.plot(months, sales, color = "teal", marker = "o")
plt.grid(axis = "y", color = "lightgray", ls = "--")
sns.despine()
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales -- Clean Style")
plt.show()
# No need for so much effort when we have this thing called smart work
# Removing Spines makes the chart look more proessional
