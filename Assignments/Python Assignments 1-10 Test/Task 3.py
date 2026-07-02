
# Task 3
# Task 3 Shop Sales Summary (Unseen Task)
# You run a small shop. Here is one week of daily sales data:
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# sales = [1200, 980, 1350, 870, 1500, 2100, 1800]
# Write a Python program that:
# 1. Stores sales as a NumPy array
# 2. Prints total sales for the week
# 3. Prints the best day (highest sales) and worst day (lowest sales)
# 4. Prints the average daily sales rounded to 2 decimal places
# 5. Creates a pandas DataFrame with columns "Day" and "Sales"
# 6. Adds a new column "Above_Average" which is True if that day&#39;s
# sales are above the weekly average
# 7. Prints the full DataFrame

# Begin your work here

import numpy as np
import pandas as pd
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sales = np.array([1200, 980, 1350, 870, 1500, 2100, 1800])
total_sales = sales.sum()
print(f"The total sales for the week are: {total_sales}")

highest_sales = max(sales)
lowest_sales = min(sales)
print(f"The highest sales were: {highest_sales}, The lowest sales were: {lowest_sales}.")

mean_sales = np.mean(sales)
print(f"The mean of the daily sales is: {mean_sales}")

df = pd.DataFrame({
    "Day" : ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Sales" : [1200, 980, 1350, 870, 1500, 2100, 1800]
})

df["Above_Average"] = df["Sales"] > mean_sales
print(df)
