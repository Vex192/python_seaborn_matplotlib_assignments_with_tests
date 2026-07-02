
# Assignment# 5

# Generate 200 random ages using: np.random.randint(18, 70, 200)
# Plot a histogram with 15 bins.
# Add a vertical red dashed line at the mean age.
# Label that line in the legend.
# Describe the shape: is it even, or does it lean one way?

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

random_ages = np.random.randint(18, 70, 200)
mn = np.mean(random_ages)
plt.hist(random_ages, bins=15)
plt.axvline(mn, color='red', linestyle='--', label="Mean Line")
plt.legend()
plt.show()
print("The shape of the mean line is even.")
