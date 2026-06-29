import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Fill missing values with 'Unknown'
df.fillna("Unknown", inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Keep date_added column unchanged

# Save the cleaned dataset
df.to_excel("netflix_titles_cleaned.xlsx", index=False)

print("Data cleaning completed successfully!")
