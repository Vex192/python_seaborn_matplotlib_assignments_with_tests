
# Task 1
# You are given the following test scores for 10 students:
# [72, 85, 90, 60, 78, 95, 55, 88, 74, 82]
# Write a Python program that:
# 1. Stores the scores as a NumPy array
# 2. Prints the mean, median, highest score, lowest score, and standard deviation
# 3. Prints this sentence using an f-string:
# "The class average is X and the top score is Y."
# (replace X and Y with the actual calculated values, rounded to 1 decimal)

# Begin your work here

import numpy as np
test_scores = np.array([72, 85, 90, 60, 78, 95, 55, 88, 74, 82])
mean = np.mean(test_scores).round(2)
median = np.median(test_scores)
std= np.std(test_scores).round(2)
highest = max(test_scores)
lowest = min(test_scores)
print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std}, Highest: {highest}, Lowest: {lowest}")
print(f"The class average is {mean} and the top score is {highest}.")
