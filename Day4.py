#Prepare Sample Data (CSV File)
import pandas as pd

# Load data
df = pd.read_csv("grades.csv")

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Fill missing values with average of the column
df.fillna(df.mean(numeric_only=True), inplace=True)

# Exploratory Data Analysis (EDA)
# Basic statistics
print(df.describe())

# Average score per student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
print(df[["Name", "Average"]])

# Visualisation
import matplotlib.pyplot as plt

# Bar chart of average scores
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.title("Average Student Scores")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()

