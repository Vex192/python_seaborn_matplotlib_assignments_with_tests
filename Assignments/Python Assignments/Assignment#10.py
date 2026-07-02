
#
#
# Assignment #10

# Using the tips dataset, answer each question with groupby:
# 1. Which day has the highest average total_bill?
# 2. Do smokers or non-smokers tip more on average?
# 3. Which meal time (Lunch or Dinner) has the higher average bill?
# Print each answer as a clear sentence.
# Write one sentence about what surprised you.

# Begin your work here

import seaborn as sns
df = sns.load_dataset("tips")
print(df.groupby("day")["total_bill"].mean().sort_values(ascending = False), "\n\n")
print(df.groupby("smoker")["tip"].mean(), "\n\n")
print(df.groupby("time")["total_bill"].mean().sort_values(ascending = False))

dinner_mean = df.loc[df["time"] == "Dinner", "total_bill"].mean()
lunch_mean = df.loc[df["time"] == "Lunch", "total_bill"].mean()

if dinner_mean > lunch_mean:
    print("Dinner has a higher average bill.")
else:
    print("Lunch has a higher average bill.")

print(df)
