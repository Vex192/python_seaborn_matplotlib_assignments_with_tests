
# Assignment# 11

# Create the bar chart from Exercise 3 again, but this time:
# Set figure size to (10, 5) — wide and short
# Set dpi=150 for higher resolution
# Then create it again at (4, 6) — tall and narrow.
# How does the shape of the figure change how the chart feels?
# Which size looks better for a bar chart?

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

x_values = ["Math", "Science", "English", "History", "Art"]
y_values = np.array([88, 75, 92, 60, 85])

plt.figure(figsize = (10, 5), dpi = 150)
plt.bar(x_values, y_values, color = ["red", "blue", "green", "orange", "purple"])
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.title("Subject Scores, Wide Bar Graph")
plt.show()
print("The English bar is the highest.")

plt.figure(figsize = (4, 6), dpi = 150)
plt.bar(x_values, y_values, color = ["red", "blue", "green", "orange", "purple"])
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.title("Subject Scores, Long Bar Graph")
plt.show()
print("The English bar is the highest.")
