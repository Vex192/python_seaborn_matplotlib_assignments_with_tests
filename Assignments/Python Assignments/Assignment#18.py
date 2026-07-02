
# Assignment #18

# From the tips dataset, compute the mean and median of total_bill.
# Now manually add one fake row where total_bill = 500.
# Recompute the mean and median.
# Which one changed more — mean or median?
# Write 2 sentences: Which is the better measure of a typical bill, and why?

# Begin your work here

import seaborn as sns
import pandas as pd

df = sns.load_dataset("tips")
mn = df["total_bill"].mean()
md = df["total_bill"].median()
df.loc[len(df), "total_bill"] = 500
new_mn = df["total_bill"].mean()
new_md = df["total_bill"].median()
print(f"Old mean: {mn.round(2)} vs. New mean: {new_mn.round(2)} || Old median: {md.round(2)} vs. New median: {new_md.round(2)}")
print("The mean changed more than the median")
print("Median is a more better measure of a typical bill because it is less sensitive to outliers.")
