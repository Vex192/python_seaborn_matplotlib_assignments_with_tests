
# Assignment# 19

# Create a bar chart with 6 bars using 6 different ways to specify color:
# 1. A named color: "teal"
# 2. A hex code: "#FF5733"
# 3. An RGB tuple: (0.2, 0.6, 0.8)
# 4. A color from a colormap: plt.cm.Set2(0)
# 5. "tomato"
# 6. "mediumseagreen"
#
# Label each bar with its color name as the x-tick.

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

labels = ["Teal", "Hex", "RGB", "CMAP", "Tomato", "Seagreen"]
nums = np.array([1, 2, 3, 4, 5, 6])

plt.bar(labels, nums, color = ["teal", "#FF5733", (0.2, 0.6, 0.8), plt.cm.Set2(0), "tomato", "mediumseagreen"])
plt.title("6 Ways To Color A Bar")
plt.show()
# Why use x ticks when u can use labels same output diff method
