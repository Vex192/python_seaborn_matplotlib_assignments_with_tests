
# Assignment# 2

# Plot the same data as Exercise 1, but now style it:
# Line color: red
# Marker style: circle (o)
# Line style: dashed (--)
# Line width: 2
# Then try changing each property to something different.
# What does marker="s" give you?

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

x_values = np.array([1, 2, 3, 4, 5])
y_values = np.array([2, 4, 1, 5, 3])

plt.plot(x_values, y_values, marker = "s", ls = "--", lw = 2, c = "red")
plt.show()
print("marker = s makes the marker at each point a square.")
