
# Assignment #8

# Using the tips dataset:
# 1. Show only bills where total_bill &gt; 25
# 2. Show only Saturday records
# 3. Show records where person is a non-smoker AND bill is over 20
# Print how many rows match each filter.
# Which filter gives the fewest rows?

# Begin your work here

import seaborn as sns
df = sns.load_dataset("tips")

bill_greater_than_25 = df[df["total_bill"] > 25]
day_is_sat = df[df["day"] == "Sat"]
non_smoker_and_bill_greater_than_20 = df[(df["smoker"] == "No") & (df["total_bill"] > 20)]

print("Bills > 25:", len(bill_greater_than_25))
print("Saturday records:", len(day_is_sat))
print("Non-smoker and bill > 20:", len(non_smoker_and_bill_greater_than_20))
