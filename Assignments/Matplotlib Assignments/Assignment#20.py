
# Assignment# 20

# Load the Titanic dataset. Create a 2x2 subplot dashboard showing:
# 1. Bar chart: survival count (survived vs not)
# 2. Bar chart: average age by passenger class
# 3. Histogram: age distribution
# 4. Bar chart: survival rate by sex
# Add a title to each subplot.
# Add a main title: "Titanic Data Dashboard".
# Use plt.tight_layout().

# Begin your work here

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset("titanic")

plt.figure(figsize = (12, 6))

plt.subplot(2, 2, 1)
survived = df["survived"].sum()
not_survived = int(df["survived"].count() - survived)
plt.bar(["Survived", "Not Survived"], [survived, not_survived], ec = "black")
plt.title("Survived vs. Died")

plt.subplot(2, 2, 2)
md = np.median(df["age"])
df.fillna({"age" : md}, inplace = True)
age_mn = df.groupby("pclass")["age"].mean()
plt.bar(age_mn.index, age_mn, ec = "black")
plt.xticks([1, 2, 3])
plt.title("Average Age By Pclas")

plt.subplot(2, 2, 3)
plt.hist(df["age"], bins = 15, ec = "black")
plt.title("Age Distribution")

plt.subplot(2, 2, 4)
survival_rate = df.groupby("sex")["survived"].mean()
plt.bar(survival_rate.index, survival_rate.values, color = ["steelblue", "hotpink"], ec = "black")
plt.title("Survival Rate")

plt.suptitle("Titanic Data Dashboard")
plt.tight_layout()
plt.show()
