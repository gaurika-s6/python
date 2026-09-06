import numpy as np
import pandas as pd

# ------------------ 1D ARRAY ------------------
arr = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(arr)

# Indexing
print("\nIndexing:")
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("\nSlicing:")
print("Elements from index 1 to 3:", arr[1:4])
print("First three elements:", arr[:3])
print("Elements from index 2 onwards:", arr[2:])

# Basic Operations
print("\nBasic Operations:")
print("Sum =", np.sum(arr))
print("Mean =", np.mean(arr))
print("Maximum =", np.max(arr))
print("Minimum =", np.min(arr))


# ------------------ 2D ARRAY ------------------
arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n\n2D Array:")
print(arr2d)

# Indexing
print("\n2D Array Indexing:")
print("Element at row 0, column 1:", arr2d[0, 1])
print("Element at row 2, column 2:", arr2d[2, 2])

# Slicing
print("\n2D Array Slicing:")
print("First row:", arr2d[0])
print("Second column:", arr2d[:, 1])
print("First two rows:")
print(arr2d[:2, :])

# Basic Operations
print("\n2D Array Operations:")
print("Shape =", arr2d.shape)
print("Transpose:")
print(arr2d.T)
print("Sum =", np.sum(arr2d))
print("Row-wise Sum =", np.sum(arr2d, axis=1))
print("Column-wise Sum =", np.sum(arr2d, axis=0))


# ------------------ PANDAS DATASET ------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("\n\nDataset:")
print(df)

# Column Access
print("\nNames Column:")
print(df["Name"])

# Row Indexing
print("\nFirst Row:")
print(df.iloc[0])

# Row and Column Selection
print("\nName and Marks of Second Student:")
print(df.loc[1, ["Name", "Marks"]])

# Slicing
print("\nFirst Two Rows:")
print(df.iloc[:2])

print("\nRows 1 to 3 and Columns Name & Age:")
print(df.loc[1:3, ["Name", "Age"]])

# Filtering
print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

# Basic Dataset Operations
print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())