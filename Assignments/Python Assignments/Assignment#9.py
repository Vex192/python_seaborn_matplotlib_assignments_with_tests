
# Assignment #9

# In the tips dataset:
# 1. Create column "tip_pct" = (tip / total_bill x 100) rounded to 1 decimal
# 2. Create column "generous" = True if tip_pct &gt; 20
# 3. How many generous tippers are there?
# 4. What percentage of ALL diners is that?
# Print the answer as a sentence.

# Begin your work here

import seaborn as sns
df = sns.load_dataset("tips")
print(df)
df["tip_pct"] = (df["tip"] / df["total_bill"] * 100).round(1)
df["generous"] = df["tip_pct"] > 20
generous_count = df["generous"].sum()
percent = generous_count / len(df) * 100
print(f"There are {generous_count} generous tippers, which is {percent:.2f}% of all diners.")
