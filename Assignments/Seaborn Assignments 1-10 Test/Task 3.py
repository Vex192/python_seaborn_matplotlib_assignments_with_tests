
# Task
# Load the Titanic dataset:
#
# df = sns.load_dataset("titanic")
#
# Write a Python program that creates ONE figure with
#
# TWO charts side by side using plt.subplots(1, 2, figsize=(12, 5)):
#
# Left chart — Box Plot:
#
# • sns.boxplot() of passenger age grouped by pclass
#
# • Use x="pclass", y="age"
#
# • Use "pastel" palette
#
# • Title: "Age Distribution by Class"
#
# • Axis labels
#
# Right chart — Count Plot:
#
# • sns.countplot() showing passenger count per class
#
# • Add hue="survived" to split by survival
#
# • Use "Set1" palette
#
# • Title: "Survival Count by Class"
#
# • Axis labels
#
# • Add main figure title: "Titanic — Class Analysis"
#
# • Use plt.tight_layout() before plt.show()
#
# Write 2 sentences as comments answering:
#
# Which class had the youngest average passengers?
#
# Which class had the best survival count?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

plt.figure(figsize = (12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(data  =  df, x  =  "pclass", y  =  "age", palette  =  "pastel")
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.title("Age Distribution by Class")

plt.subplot(1, 2, 2)
sns.countplot(data = df, x = "pclass", hue = "survived", palette = "Set1")
plt.xlabel("Passenger Class")
plt.legend(title = "Survival Status", labels = ["Survived", "Not Survived"])
plt.title("Survival Count by Class")

plt.suptitle("Titanic — Class Analysis", y = 0.98, fontsize = 16)
plt.tight_layout()
plt.show()
# Pclass 3 has youngest average passengers. Pclass 3 also has the most survival count
