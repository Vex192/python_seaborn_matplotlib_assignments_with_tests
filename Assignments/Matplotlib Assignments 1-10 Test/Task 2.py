
# Task
# Write a Python program that:
# 1. Generates 200 random ages using:
# np.random.randint(18, 70, 200)
# 2. Plots a histogram of these ages using 15 bins
# 3. Uses steelblue as the bar color with white edges
# 4. Adds a vertical RED dashed line at the mean age
# 5. Labels that line in the legend showing the actual mean value
# Example: "Mean: 43.2"
# 6. Adds a title: "Age Distribution"
# 7. Adds x-axis label: "Age" and y-axis label: "Count"
# 8. Shows the legend and displays the chart
# Look at your histogram — is the distribution symmetric or skewed?
# Write your answer as a comment in your code.

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

random_ages = np.random.randint(18, 70, 200)
mn = np.mean(random_ages)

plt.hist(random_ages, bins = 15, color = "steelblue")
plt.axvline(float(mn), color = "red", ls = "--", label = "Mean Line")
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age DIstribution")
plt.legend()
plt.show()
# The distribution is symmetrical because the ages are almost the same height on the histogram
