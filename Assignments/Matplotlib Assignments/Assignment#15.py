
# Assignment# 15

# Create a weekly temperature chart for 4 weeks (28 days) using random values between 15 and
# 35.
# Plot it as a line chart.
# Then use plt.fill_between() to shade the area under the line in light blue with alpha=0.3.
# Also add a horizontal dashed line at 25 (comfortable temperature).
# Label that line in the legend.

# Begin your work here

import matplotlib.pyplot as plt
import numpy as np

days = list(range(1, 29))
random_temps = np.random.randint(15, 35, 28)

plt.plot(days , random_temps, color = "steelblue")
plt.fill_between(days, random_temps, color = "steelblue", alpha = 0.3)
plt.axhline(25, color = "red", ls = "--", label = "Comfortable Temperature 25C")
plt.xlabel("Days")
plt.ylabel("Temperature (C)")
plt.legend()
plt.show()
