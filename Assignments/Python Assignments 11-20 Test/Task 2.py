
# Task
# Load the tips dataset using:
#
# import seaborn as sns
#
# df = sns.load_dataset("tips")
#
# Write a Python program that:
# 1. Prints the mean and median of the "total_bill" column
# 2. Creates a new DataFrame that adds ONE fake row where
# total_bill = 500 (make up values for the other columns)
# 3. Prints the NEW mean and NEW median after adding that row
# 4. Prints which value changed more — mean or median
# 5. Writes ONE sentence in a print statement explaining
# why median is better for describing a typical bill

# Begin your work here

import seaborn as sns

df = sns.load_dataset("tips")

mn = df["total_bill"].mean().round(2)
md = df["total_bill"].median()
df.loc[len(df)] = [500, 50.0, "Male", "No", "Sun", "Dinner", 5]
new_mn = df["total_bill"].mean().round(2)
new_md = df["total_bill"].median()
change_mean = abs(new_mn - mn)
change_md = abs(new_md - md)
print(f"Old Mean: {mn} vs. New Mean: {new_mn} || Old Median: {md} vs. New Median: {new_md}")
if change_mean > change_md:
    print("Mean changed more than median.")
elif change_md > change_mean:
    print("Median changed more than mean.")
else:
    print("Mean and median changed by the same amount.")
print("Median is better for describing a typical bill because it is less affected by the extreme $500 value and better represents the typical bill amount.")
