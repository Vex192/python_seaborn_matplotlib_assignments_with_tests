
# Assignment# 8

# Create a pie chart for phone market share:
# brands = ["Samsung","Apple","Xiaomi","Others"]
# shares = [32, 28, 15, 25]
# Show the percentage on each slice using autopct.
# Explode (pull out) the largest slice slightly.
# Add a title.

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

brands = ["Samsung", "Apple", "Xiaomi", "Others"]
shares = [32, 28, 15, 25]

plt.pie(shares, labels=brands, autopct="%1.1f%%", explode=(0.1, 0, 0, 0))
plt.title("Phone Market Share")
plt.show()
