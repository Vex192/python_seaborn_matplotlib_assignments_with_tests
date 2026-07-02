
# Assignment #12

# Using the Titanic dataset:
# 1. Find survival rate by passenger class (pclass)
# 2. Find survival rate by sex
# 3. How many passengers were in each class?
# Print your findings clearly.
# Write 2 sentences: What pattern do you notice? Why do you think that happened?

# Begin your work here

import seaborn as sns
df = sns.load_dataset("titanic")
pclass_survived = df.groupby("pclass")["survived"].mean().round(3)
sex_survived = df.groupby("pclass")["survived"].mean().round(3)
count_pclass = df["pclass"].value_counts()
print(pclass_survived, sex_survived, count_pclass)
