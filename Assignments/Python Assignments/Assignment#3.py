
# Assignment #3

# Daily temperatures in Celsius for one week: [22, 19, 25, 30, 27, 18, 23].
# Convert ALL of them to Fahrenheit using: F = C x 9/5 + 32
# Do this without any loop — apply the formula to the whole array.
# Print both arrays side by side.
# Which day was the hottest in Fahrenheit?

# Begin your work here

# import numpy and make the list
import numpy as np
daily_temp_for_one_week_in_celsius = np.array([22, 19, 25, 30, 27, 18, 23])
# apply formula
daily_temp_for_one_week_in_farenheit = daily_temp_for_one_week_in_celsius * 9/5 + 32
# print side by side
print(daily_temp_for_one_week_in_celsius)
print(daily_temp_for_one_week_in_farenheit)
# find hottest day and print
hottest_in_farenheit = max(daily_temp_for_one_week_in_farenheit)
print(f"The hottest day in farenheit was {hottest_in_farenheit}")
