
# Assignment# 6

# Generate fake height and weight data for 50 people:
# heights = np.random.randint(150, 190, 50) (cm)
# weights = heights * 0.45 + np.random.randint(-10, 10, 50) (kg)
# Plot a scatter chart. Set alpha=0.6 so overlapping dots show through.
# Add a title and axis labels.
# Do you see a pattern between height and weight?

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

heights = np.random.randint(150, 190, 50)
weights = weights = heights * 0.45 + np.random.randint(-10, 10, 50)

plt.scatter(heights, weights, alpha = 0.6)
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Random Heights And Weights")
plt.show()
print("It seems that the more the weight is the more the height.")
