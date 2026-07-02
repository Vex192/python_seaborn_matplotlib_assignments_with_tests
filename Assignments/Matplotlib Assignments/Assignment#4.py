
# Assignment# 4

# Create a horizontal bar chart of top 5 countries by population (use made-up numbers).
# Countries: ["China","India","USA","Indonesia","Pakistan"]
# Populations (millions): [1400, 1380, 330, 275, 230]
# Add value labels at the end of each bar using plt.text().
# When is a horizontal bar chart better than a vertical one?

# Begin your work here

import matplotlib.pyplot as plt
x_values = ["China", "India", "USA", "Indonesia", "Pakistan"]
y_values = [1400, 1380, 330, 275, 230]
bars = plt.barh(x_values, y_values)
plt.bar_label(bars)
plt.show()
print("A horizontal bar chart is better than a vertical bar chart when the category labels are long.")
