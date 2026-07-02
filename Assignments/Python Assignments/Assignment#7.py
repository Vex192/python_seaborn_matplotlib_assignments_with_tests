
# Assignment #7

# Load the tips dataset: import seaborn as sns then df = sns.load_dataset("tips")
# Answer these questions using code:
# 1. How many rows and columns does it have?
# 2. What are the column names?
# 3. What does df.describe() show you?
# 4. What is the most common day people eat out?

# Begin your work here

import seaborn as sns
df = sns.load_dataset("tips")
print(df.shape)
print(df.columns, "\n\n")
print(df.describe(), "\n\n")
print(df["day"].value_counts())
