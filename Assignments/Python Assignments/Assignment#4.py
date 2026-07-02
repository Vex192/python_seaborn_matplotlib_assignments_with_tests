
# Assignment #4

# Simulate rolling a 6-sided die 100 times using np.random.randint(1, 7, 100).
# Count how many times you rolled a 6.
# Count how many times you rolled an even number (hint: use % 2 == 0).
# Print both results.
# Run the program again — do the numbers change? Why?

# Begin your work here

# simulate rolling a six sided die 100 times and import numpy
import numpy as np
simulation = np.random.randint(1, 7, 100)
# find the count of sixes and even and print
count_sixes = np.sum(simulation == 6)
print(f"Number of sixes: {count_sixes}")
count_even = np.sum(simulation % 2 == 0)
print(f"Number of even: {count_even}")
