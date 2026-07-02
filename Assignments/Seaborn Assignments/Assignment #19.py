
# Assignment #19

# Explore Seaborn color palettes:
#
# 1. Plot a bar chart using palette="Set1"
#
# 2. Plot the same chart using palette="pastel"
#
# 3. Plot using palette="coolwarm"
#
# 4. Plot using palette="husl"
#
# Print all available palettes: sns.color_palette()
#
# Which palette works best for categorical data?
#
# Which for sequential (low to high) data?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

fig, axes = plt.subplots(2, 2, figsize = (12, 6))

sns.barplot(data = df, x = "day", y = "total_bill", palette = "Set1", ax = axes[0, 0])
axes[0, 0].set_xlabel("Days")
axes[0, 0].set_xlabel("Total Bill")
axes[0, 0].set_title("Total Bill By Days, Pallete : Set1")

sns.barplot(data = df, x = "day", y = "total_bill", palette = "pastel", ax = axes[0, 1])
plt.xlabel("Days")
plt.ylabel("Total Bill")
axes[0, 1].set_xlabel("Days")
axes[0, 1].set_xlabel("Total Bill")
axes[0, 1].set_title("Total Bill By Days, Pallete : pastel")

sns.barplot(data = df, x = "day", y = "total_bill", palette = "coolwarm", ax = axes[1, 0])
plt.xlabel("Days")
plt.ylabel("Total Bill")
axes[1, 0].set_xlabel("Days")
axes[1, 0].set_xlabel("Total Bill")
axes[1, 0].set_title("Total Bill By Days, Pallete : coolwarm")

sns.barplot(data = df, x = "day", y = "total_bill", palette = "husl", ax = axes[1, 1])
plt.xlabel("Days")
plt.ylabel("Total Bill")
axes[1, 1].set_xlabel("Days")
axes[1, 1].set_xlabel("Total Bill")
axes[1, 1].set_title("Total Bill By Days, Pallete : husl")

plt.suptitle("Total Bill By Days With Different Palletes", fontsize = 16)
plt.tight_layout()
plt.show()
