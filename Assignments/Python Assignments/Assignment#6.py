
# Assignment #6

# Create a DataFrame with 6 students.
# Columns: Name, Math, Science, English (scores out of 100).
# Add a new column "Average" = mean of the three subjects, rounded to 1 decimal.
# Add a column "Pass" = True if Average &gt;= 60.
# Print the full DataFrame.
# How many students passed?

# Begin your work here

import pandas as pd
df = pd.DataFrame({
    "Name" : ["Ali", "Wali", "Shan", "Ahad"],
    "Math" : [100, 85, 60, 90],
    "Science" : [95, 89, 70, 87],
    "English" : [96, 85, 79, 85]
})

df["Average"] = (df["Math"] + df["Science"] + df["English"] / 3).round(1)
df["Pass"] = df["Average"] >=60
print(df)
