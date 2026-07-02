
# Task
# You have this data for 6 months:
#
# months = ["Jan","Feb","Mar","Apr","May","Jun"]
#
# sales = [8000, 9500, 11000, 13000, 15000, 14000]
#
# temperature = [5, 8, 14, 20, 27, 32]
#
# Write a Python program that:
#
# 1. Creates a figure using fig, ax1 = plt.subplots(figsize=(10, 5))
# 2. Creates a second y-axis using ax2 = ax1.twinx()
# 3. Plots sales as a BLUE bar chart on ax1 (left y-axis)
# 4. Plots temperature as a RED line with circle markers on ax2
# (right y-axis)
#
# 5. Labels left y-axis: "Sales ($)"
# 6. Labels right y-axis: "Temperature (C)"
# 7. Labels x-axis: "Month"
# 8. Adds title: "Sales vs Temperature — 6 Months"
# 9. Shows the chart
#
# Write one sentence as a comment: what pattern do you notice
# between sales and temperature in this data?
#
# Your Code:

# Begin your work here

import matplotlib.pyplot as plt
import pandas as pd

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df = pd.DataFrame({
    "Sales" : [8000, 9500, 11000, 13000, 15000, 14000],
    "Temperature" : [5, 8, 14, 20, 27, 32],
}, index = months)

df["Sales"].plot(kind = "bar", color = "blue", ec = "black", ylabel = "Sales")
df["Temperature"].plot(secondary_y = True, color = "red", marker = "o", ylabel = "Temperature")
plt.xlabel("Months")
plt.title("Sales vs Temperature — 6 Months")
plt.show()
# they both rise up as months go by
