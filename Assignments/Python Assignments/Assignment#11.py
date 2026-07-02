
# Assignment #11

# Load Titanic: df = sns.load_dataset("titanic")
# 1. Count missing values per column — which column is worst?
# 2. Fill missing "age" values with the median age
# 3. Drop rows where "embark_town" is missing
# 4. Confirm both columns now have 0 missing values
# Print before and after counts.

# Begin your work here

import seaborn as sns
df = sns.load_dataset("titanic")
print("Deck column has the most null values and so it is the worst.")
md = df["age"].median()
df.fillna({"age": md}, inplace = True)
df.dropna(subset = ["embark_town"], inplace = True)
print(df.isnull().sum())
