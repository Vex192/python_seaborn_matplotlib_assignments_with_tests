
# Assignment #5

# Load the Titanic dataset.
#
# Create a count plot showing how many passengers were in each class:
#
# sns.countplot(x="pclass", data=df)
#
# Then add hue="survived" to split each bar by survival.
#
# No need to count manually — Seaborn does it automatically.
#
# What do you notice about survival rates by class?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

sns.countplot(data = df, x = "pclass", hue = "survived")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.title("Count of Passengers by Class and Survival Status")
plt.legend(title = "Survival Status", loc = "upper left", labels = ["Survived", "Not Survived"])
plt.show()
