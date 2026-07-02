
# Assignment #5

# Class A scores: [88, 72, 95, 60, 78, 85, 91, 70]
# Class B scores: [75, 80, 68, 90, 77, 83, 71, 88]
# Find the mean and standard deviation of each class.
# Which class performed better on average?
# Which class was more consistent? (Hint: lower std = more consistent)
# Print your conclusions as sentences.

# Begin your work here

import numpy as np
class_a_scores = [88, 72, 95, 60, 78, 85, 91, 70]
mean_a = np.mean(class_a_scores)
print(f"Mean of class A scores are: {mean_a.round(2)}")
std_a = np.std(class_a_scores)
print(f"Standard deviation of class A scores are: {std_a.round(2)}")
class_b_scores = [75, 80, 68, 90, 77, 83, 71, 88]
mean_b = np.mean(class_b_scores)
print(f"Mean of class A scores are: {mean_b.round(2)}")
std_b = np.std(class_b_scores)
print(f"Standard deviation of class A scores are: {std_b.round(2)} \n\n")
if mean_a > mean_b:
    print("Class A performed better than Class B on average.")
else:
    print("Class B performed better than Class C on average.")

if std_a < std_b:
    print("Class A was more consistent than Class B.")
else:
    print("Class B was more consistent than Class A.")
