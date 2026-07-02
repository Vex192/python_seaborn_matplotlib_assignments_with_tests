
# Assignment# 14

# Create a stacked bar chart showing sales by quarter for two products:
#
# quarters = ["Q1","Q2","Q3","Q4"]
#
# product_a = [4000, 4500, 5000, 6000]
#
# product_b = [3000, 3200, 2800, 3500]
#
# Stack product_b on top of product_a.
# Add a legend and title.
# When is a stacked bar chart useful?

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

quarters = ["Q1", "Q2", "Q3", "Q4"]
product_a = np.array([4000, 4500, 5000, 6000])
product_b = np.array([3000, 3200, 2800, 3500])

plt.bar(quarters, product_a, color = "skyblue", ec = "black", label = "Product A")
plt.bar(quarters, product_a, color = "red", ec = "black", label = "Product B", bottom = product_a)
plt.legend(title = "Product Names")
plt.title("Stacker Bar Chart For Two Products")
plt.show()
