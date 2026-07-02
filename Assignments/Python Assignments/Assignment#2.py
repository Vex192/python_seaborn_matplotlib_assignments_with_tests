
# Assignment #2

# Scores for 10 students: [72, 85, 90, 60, 78, 95, 55, 88, 74, 82].
# Find: mean, median, highest score, lowest score, and standard deviation.
# Then print a sentence: "The class average is X and the top score is Y."
# Round all values to 1 decimal place.

# Begin your work here

# import numpy and make list
import numpy as np
scores = np.array([72, 85, 90, 60, 78, 95, 55, 88, 74, 82])
# find mean, median, highest score, lowest score, and standard deviation.
mean = np.mean(scores).round(1)
median = np.median(scores)
std = np.std(scores).round(1)
highest = max(scores)
lowest = min(scores)
print(f"The class average is {mean} and the top score is {highest}.")
