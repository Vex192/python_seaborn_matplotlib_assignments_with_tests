
# Assignment# 9

# Plot two lines on the same chart:
#
# months = [1,2,3,4,5,6,7,8,9,10,11,12]
#
# store_a = [4000,4200,3800,5000,5500,6000,5800,6200,6500,7000,6800,7500]
#
# store_b = [3500,3700,4100,4300,4800,5100,5300,5600,5900,6100,6400,6700]
#
# Use different colors and line styles for each.
# Add a legend so the viewer knows which line is which.

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
store_a = np.array([4000, 4200, 3800, 5000, 5500, 6000, 5800, 6200, 6500, 7000, 6800, 7500])
store_b = np.array([3500, 3700, 4100, 4300, 4800, 5100, 5300, 5600, 5900, 6100, 6400, 6700])

plt.plot(store_a, marker = "o", ls = "-", lw = 2, label = "Store A")
plt.plot(store_b, marker = "o", ls = "-", lw = 2, label = "Store B")
plt.legend()
plt.show()
