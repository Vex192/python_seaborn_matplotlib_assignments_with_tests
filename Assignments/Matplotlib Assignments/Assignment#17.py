
# Assignment# 17

# Create any chart you like — bar, line, or scatter.
# Save it as a PNG file called "my_chart.png" using plt.savefig().
# Also save a second copy as a PDF.
# Use bbox_inches="tight" so nothing gets cut off.
# Check that both files appear in your folder.

# Begin your work here

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
store_a = np.array([4000, 4200, 3800, 5000, 5500, 6000, 5800, 6200, 6500, 7000, 6800, 7500])

plt.plot(store_a, marker = "o", ls = "-", lw = 2)
plt.grid(axis = "y", color = "lightgray", ls = "--")
plt.xlabel("Months")
plt.ylabel("Sales")
sns.despine()
plt.savefig("my_chart.png", bbox_inches = "tight")
plt.savefig("my_chart.pdf", bbox_inches = "tight")
plt.show()
