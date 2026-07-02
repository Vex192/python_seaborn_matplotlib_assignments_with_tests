
# Task
#
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
#
# city_a = [120, 95, 80, 45, 20, 10]
#
# city_b = [60, 70, 85, 90, 75, 50]
#
# Write a Python program that creates ONE figure with TWO charts
# side by side using plt.subplots(1, 2):
#
# Left chart:
#
# • Line chart of BOTH cities on the same axes
#
# • City A — blue solid line with circle markers
#
# • City B — red dashed line with square markers
#
# • Title: "Rainfall Comparison"
#
# • Axis labels and legend
#
#
# Right chart:
#
# • Bar chart showing City A rainfall only
#
# • Each bar a different shade or color
#
# • Title: "City A Monthly Rainfall"
#
# • Axis labels
#
# • Add a main title for the whole figure:
# "6-Month Rainfall Report"
#
# • Use plt.tight_layout() before plt.show()
#
#
# Scoring Guide
#
# Task 1 — Bar Chart — Subjects: 5 requirements + color + labels 30 pts
#
# Task 2 — Histogram with Mean Line: 8 requirements including legend and comment 35 pts
#
# Task 3 — Rainfall — Subplots (Unseen): Two charts, main title, tight_layout 35 pts

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
city_a = [120, 95, 80, 45, 20, 10]
city_b = [60, 70, 85, 90, 75, 50]

plt.subplot(1, 2, 1)

plt.plot(months, city_a, color = "blue", ls = "-", marker = "o", label = "City A")
plt.plot(months, city_b, color = "red", ls = "--", marker = "s", label = "City B")
plt.xlabel("Months")
plt.ylabel("Rainfall (cm)")
plt.title("Rainfall Comparison")
plt.legend()

plt.subplot(1, 2, 2)


plt.bar(months, city_a, color = ["red", "blue", "green", "yellow", "orange", "purple"])
plt.xlabel("Months")
plt.ylabel("Rainfall (cm)")
plt.title("City A Monthly Rainfall")

plt.suptitle("6-Month Rainfall Report")
plt.tight_layout()
plt.show()
