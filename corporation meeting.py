import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Meeting_ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Duration_Minutes": [30, 45, 60, 90, 120, 50, 40, 80],
    "Productivity_Score": [8, 7, 6, 4, 3, 7, 8, 5]
}

df = pd.DataFrame(data)
print(df)
print("\nSummary Statistics:")
print(df.describe())
average_productivity = df.groupby("Duration_Minutes")["Productivity_Score"].mean()
print("\nAverage Productivity by Meeting Duration:")
print(average_productivity)
plt.hist(df["Duration_Minutes"], bins=5, edgecolor="black")
plt.xlabel("Meeting Duration (minutes)")
plt.ylabel("Number of Meetings")
plt.title("Distribution of Meeting Durations")
plt.show()
plt.hist(df["Productivity_Score"], bins=5, edgecolor="black", color="green")
plt.xlabel("Productivity Score")
plt.ylabel("Frequency")
plt.title("Distribution of Productivity Scores")
plt.show()
