import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("Titanic-Dataset.csv")

print(df.head())
print(df.info())

### DATA CLEANING ###
# Remove rows where the 'Age' column has missing (NaN) values
df = df.dropna(subset=['Age'])

# Convert all names to lowercase letters for consistency
df['Name'] = df['Name'].str.lower()

# Convert all entries in the 'Sex' column to lowercase letters
df['Sex'] = df['Sex'].str.lower()

# Fill missing values in the 'Embarked' column with the most common (mode) value
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Display how many missing values remain in each column after cleaning
print(df.isnull().sum())

# --- SIMPLE VISUAL CHECKS ---

# Create a histogram (bar graph) of the 'Age' column to see its distribution
df['Age'].hist()
plt.show()
# Count how many passengers are in each class (1st, 2nd, 3rd) and plot it as a bar chart
df['Pclass'].value_counts().plot(kind='bar')
plt.show()
