
# Assignment #1

# Create a NumPy array of 6 grocery item prices: [3.50, 1.20, 5.00, 2.75, 4.10, 0.99].
# Create another array of quantities: [2, 5, 1, 3, 2, 4].
# Multiply them to get the cost per item.
# Print the total bill using .sum().
# Then apply a 10% discount and print the new total.

# Begin your work here

# first we import numpy
import numpy as np
# then we make the lists
prices = np.array([3.50, 1.20, 5.00, 2.75, 4.10, 0.99])
qty    = np.array([2, 5, 1, 3, 2, 4])
# we multiply them by each other to get the cost per item easily
cost_per_item = prices * qty
# finally we print the total and the total with discount of 10%
print(f"Total : {cost_per_item.sum().round(2)}")
print(f"Total with discount : {cost_per_item.sum() * 0.90}")
