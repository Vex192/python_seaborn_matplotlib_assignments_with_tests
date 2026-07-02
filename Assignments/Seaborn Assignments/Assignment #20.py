
# Assignment #20

# Load the Titanic dataset. Build a full EDA dashboard using a 2x2 subplot grid:
#
# Top-left: countplot of pclass with hue=survived
#
# Top-right: boxplot of age by pclass
#
# Bottom-left: histplot of age with kde=True
#
# Bottom-right: heatmap of survival rate by sex and class
#
# Add titles to all 4 charts.
#
# Add a main title: "Titanic EDA Dashboard".
#
# Write 3 sentences about what you learned.

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

fig, axes = plt.subplots(2, 2, figsize = (12, 6))

sns.countplot(data = df, x = "pclass", hue = "survived", ax = axes[0, 0])
axes[0, 0].set_xlabel("Count")
axes[0, 0].set_ylabel("Age")
axes[0, 0].legend(title = "Survival Status", labels = ["Survived", "Not Survived"])
axes[0, 0].set_title("Countplot Of Age By Passenger Class")

sns.boxplot(data = df, x = "age", ax = axes[0, 1])
axes[0, 1].set_xlabel("Age")
axes[0, 1].set_title("Boxplot Of Age By Passenger Class")

sns.histplot(data = df, x = "age", bins = 20, kde = True, ax = axes[1, 0])
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_title("Boxplot Of Age By Passenger Class")

pivot = df.pivot_table(values = "survived", index = "sex", columns = "pclass", aggfunc = "mean")
sns.heatmap(pivot, annot = True, fmt = ".0%", cmap = "coolwarm", ax = axes[1, 1])
axes[1, 1].set_xlabel("Pclass")
axes[1, 1].set_ylabel("Sex")
axes[1, 1].set_title("Boxplot Of Age By Passenger Class")

plt.tight_layout()
plt.suptitle("Titanic EDA Dashboard", y = 1.02, fontsize = 16)
plt.show()
