import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("student_exam_scores.csv")

print("Dataset loaded successfully!\n")

# 1. Display first 5 rows
print("First 5 rows:")
print(df.head())

# 2. Display last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# 3. Display shape
print("\nShape of dataset:")
print(df.shape)

# 4. Display column names
print("\nColumn names:")
print(df.columns)

# 5. Display data types
print("\nData types:")
print(df.dtypes)

# 6. Display information
print("\nDataset information:")
df.info()

# 7. Statistical summary
print("\nStatistical summary:")
print(df.describe())


# Statistical operations

print("\nMean of exam score:")
print(df["exam_score"].mean())

print("\nMedian of exam score:")
print(df["exam_score"].median())

print("\nMode of exam score:")
print(df["exam_score"].mode())

print("\nVariance of exam score:")
print(df["exam_score"].var())

print("\nStandard deviation of exam score:")
print(df["exam_score"].std())

print("\nMinimum exam score:")
print(df["exam_score"].min())

print("\nMaximum exam score:")
print(df["exam_score"].max())

print("\nCount of exam scores:")
print(df["exam_score"].count())


# Unique values

print("\nUnique student IDs:")
print(df["student_id"].unique())

print("\nNumber of unique student IDs:")
print(df["student_id"].nunique())

print("\nStudent ID frequency:")
print(df["student_id"].value_counts().head())


# Missing values

print("\nMissing values:")
print(df.isnull())

print("\nMissing value count:")
print(df.isnull().sum())

print("\nMissing value percentage:")
print(df.isnull().mean() * 100)

# Remove missing values
df_without_null = df.dropna()

print("\nShape after removing missing values:")
print(df_without_null.shape)

# Fill missing values
df_filled = df.fillna(0)

print("\nMissing values after filling:")
print(df_filled.isnull().sum())


# Duplicate values

print("\nDuplicate rows:")
print(df.duplicated())

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

df_clean = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df_clean.shape)


# Selecting data

print("\nExam score column:")
print(df["exam_score"])

print("\nSelecting multiple columns:")
print(df[["hours_studied", "sleep_hours", "exam_score"]])

print("\nFirst 5 rows using iloc:")
print(df.iloc[0:5])


# Conditional selection

print("\nStudents with exam score greater than 40:")
print(df[df["exam_score"] > 40])


# Sorting

print("\nDataset sorted by exam score:")
print(df.sort_values("exam_score"))


# Rename column

df = df.rename(columns={"exam_score": "Exam_Score"})

print("\nColumn names after renaming:")
print(df.columns)


# Create a new column

df["Study_Efficiency"] = df["hours_studied"] / df["sleep_hours"]

print("\nStudy efficiency:")
print(df[["hours_studied", "sleep_hours", "Study_Efficiency"]].head())


# Create performance column using NumPy

df["Performance"] = np.where(
    df["Exam_Score"] >= 35,
    "Good",
    "Needs Improvement"
)

print("\nPerformance:")
print(df[["Exam_Score", "Performance"]].head())


# Delete a column

df["Temporary"] = 1

print("\nColumns after creating temporary column:")
print(df.columns)

df = df.drop("Temporary", axis=1)

print("\nColumns after deleting temporary column:")
print(df.columns)


# Group data

print("\nNumber of students for each study hour:")
print(df.groupby("hours_studied").size())


# Group by and calculate average

print("\nAverage exam score for each study hour:")
print(df.groupby("hours_studied")["Exam_Score"].mean())


# Concatenate two parts of the dataset

df1 = df.iloc[:100]
df2 = df.iloc[100:]

combined = pd.concat([df1, df2], ignore_index=True)

print("\nShape after concatenation:")
print(combined.shape)


# Merge two dataframes

df1 = df[["student_id", "Exam_Score"]]
df2 = df[["student_id", "hours_studied"]]

merged = pd.merge(df1, df2, on="student_id")

print("\nMerged dataframe:")
print(merged.head())


# Save the final dataset

df.to_csv("students_eda_result.csv", index=False)

print("\nFinal dataset saved successfully.")

print("\nAll EDA operations completed!")