
# Assignment #20

# Using the tips dataset, do a complete mini-analysis:
# 1. Load and inspect the data (shape, describe, value_counts on day)
# 2. Add a tip_pct column = (tip / total_bill x 100)
# 3. Find average tip_pct by day using groupby
# 4. Find average tip_pct by time (Lunch vs Dinner)
# 5. Plot a bar chart of average tip_pct by day
# 6. Write 3 sentences: What did you find? What surprised you? What would you investigate next?

# Begin your work here

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
print("The shape of the dataset is: ", df.shape, "\n\n")
print("Here are some useful stats about the data: ", df.describe(), "\n\n")
print(df["day"].value_counts(), "\n\n")

df["tip_pct"] = (df["tip"]/df["total_bill"] * 100)
print("Average tip percent by day: ", df.groupby("day")["tip_pct"].mean(), "\n\n")
print("Average tip percent by time: ", df.groupby("time")["tip_pct"].mean(), "\n\n")

sns.barplot(df.groupby("day")["tip_pct"].mean())
plt.xlabel("Day")
plt.ylabel("Tip Percent")
plt.title("Average Tip Percent By Day")
plt.show()

print("I found the tip percent and its average by day and by time(dinner vs. lunch). I also found some stats about the dataset which are useful.")
print("I was surprised that all days have almost the same tip percent average by day")
print("I would investigate the correlation between the tip percent averages of by day and time.")
