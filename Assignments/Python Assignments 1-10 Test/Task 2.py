
# Task 2
# Load the tips dataset using: import seaborn as sns
# df = sns.load_dataset("tips")
#
# Write a Python program that:
# 1. Creates a new column called "tip_pct" = (tip divided by total_bill) x 100,
# rounded to 1 decimal place
# 2. Creates a column called "generous" which is True if tip_pct is greater than 20
# 3. Counts how many generous tippers there are and prints the result
# 4. Prints what percentage of ALL diners are generous tippers
# Example output: "45 generous tippers = 18.4% of all diners"

# Begin your work here

import seaborn as sns
df = sns.load_dataset("tips")
df["tip_pct"] = (df["tip"]/df["total_bill"] * 100).round(1)
df["generous"] = df["tip_pct"] > 20
generous_count = df["generous"].sum()
generous_percent = generous_count / len(df) * 100
print(f"{generous_count} generous tippers is {generous_percent:.1f}% of all diners")
