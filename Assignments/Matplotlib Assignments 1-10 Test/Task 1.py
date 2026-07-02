
# Task 1
# You have the following subject scores for a student:
#
# subjects = ["Math", "Science", "English", "History", "Art"]
#
# scores = [88, 75, 92, 60, 85]
#
# Write a Python program that:
#
# 1. Plots a bar chart of subjects vs scores
# 2. Uses a DIFFERENT color for each bar
# 3. Adds a title: "My Subject Scores"
# 4. Adds x-axis label: "Subject" and y-axis label: "Score"
# 5. Adds white edge color to each bar to separate them clearly
# 6. Displays the chart using plt.show()
# Which subject bar is the tallest? Write it as a comment in your code.

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

subjects = ["Math", "Science", "English", "History", "Art"]
scores = np.array([88, 75, 92, 60, 85])

plt.bar(subjects, scores, color = ["red", "blue", "green", "orange", "purple"], edgecolor = "black") # black edge color because white is invisible
plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("My Subject Scores")
plt.show()
# English is the tallest bar because it has the highest y value.
