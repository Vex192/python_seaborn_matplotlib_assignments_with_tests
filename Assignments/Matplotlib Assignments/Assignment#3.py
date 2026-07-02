
# Assignment# 3

# Create a bar chart showing these subject scores:
# subjects = ["Math", "Science", "English", "History", "Art"]
# scores = [88, 75, 92, 60, 85]
# Color each bar a different color.
# Add a title and axis labels.
# Which subject bar is tallest?

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

x_values = ["Math", "Science", "English", "History", "Art"]
y_values = np.array([88, 75, 92, 60, 85])

plt.bar(x_values, y_values, color = ["red", "blue", "green", "orange", "purple"])
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.title("Subject Scores")
plt.show()
print("The English bar is the highest.")
