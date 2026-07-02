
# Task 1
# Load the Titanic dataset using:
#
# import seaborn as sns
#
# df = sns.load_dataset("titanic")
#
# Write a Python program that:
# 1. Prints how many values are missing in EACH column
# 2. Fills all missing "age" values with the median age
# 3. Drops all rows where "embark_town" is missing
# 4. Prints the missing value count for "age" and "embark_town"
# AFTER cleaning — confirm both are now 0
# 5. Prints the shape of the DataFrame before and after cleaning

# Begin your work here

import seaborn as sns
df = sns.load_dataset("titanic")
print("Before cleaning:\n\n", df.isnull().sum(), "\n\n")
print("Shape before cleaning:", df.shape)
md = df["age"].median()
df.fillna({"age" : md}, inplace = True)
df.dropna(subset = "embark_town", inplace = True)
print("After cleaning:\n\n", df.isnull().sum())
print("Shape after cleaning:", df.shape)
