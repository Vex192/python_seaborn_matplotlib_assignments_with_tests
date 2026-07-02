
# Task
# A bookstore recorded its weekly sales for 4 genres. Create this
# DataFrame yourself using the data below:
#
# Genre: ["Fiction", "Science", "History", "Comics"]
#
# Mon: [120, 85, 60, 200]
#
# Tue: [95, 110, 45, 180]
#
# Wed: [140, 75, 80, 220]
#
# Thu: [100, 90, 55, 195]
#
# Fri: [160, 130, 70, 250]
#
# Write a Python program that:
#
# 1. Creates the DataFrame with Genre as the index
# 2. Adds a column "Total" = sum of all 5 days for each genre
# 3. Adds a column "Daily_Avg" = Total divided by 5, rounded to 1 decimal
# 4. Prints which genre had the highest total sales
# 5. Prints which day had the highest sales across ALL genres combined
# 6. Prints the full DataFrame sorted by Total sales, highest first

# Begin your work here

import pandas as pd

df = pd.DataFrame({
    "Genre" : ["Fiction", "Science", "History", "Comics"],
    "Mon" : [120, 85, 60, 200],
    "Tue" : [95, 110, 45, 180],
    "Wed" : [140, 75, 80, 220],
    "Thu" : [100, 90, 55, 195],
    "Fri" : [160, 130, 70, 250]
})

df["Total"] = df["Mon"] + df["Tue"] + df["Wed"] + df["Thu"] + df["Fri"]
df["Daily_Avg"] = (df["Total"] / 5).round(1)
print(f"{df.loc[df['Total'].idxmax(), 'Genre']} was the genre with the highest sales across all genres.\n\n")
print(f"{df[['Mon', 'Tue', 'Wed', 'Thu', 'Fri']].sum().idxmax()} was the day with the highest sales across all genres.\n\n")
print(df.sort_values("Total", ascending = False))
