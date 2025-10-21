# 🧠 Pandas Cheatsheet

## 🔹 Loading & Saving Data
| Function | Description |
|-----------|--------------|
| `pd.read_csv("file.csv")` | Load data from a CSV file |
| `df.to_csv("file.csv", index=False)` | Save DataFrame to a CSV file |
| `pd.read_excel("file.xlsx")` | Load Excel file |
| `pd.read_json("file.json")` | Load JSON file |

---

## 🔹 Inspecting Data
| Function | Description |
|-----------|--------------|
| `df.head(n)` | Show first n rows |
| `df.tail(n)` | Show last n rows |
| `df.info()` | Show data types and non-null counts |
| `df.describe()` | Summary stats (mean, std, min, etc.) |
| `df.shape` | Get (rows, columns) |
| `df.columns` | List all column names |
| `df.dtypes` | Show data types |

---

## 🔹 Selecting Data
| Function | Description |
|-----------|--------------|
| `df['col']` | Select one column |
| `df[['col1','col2']]` | Select multiple columns |
| `df.loc[row_index, 'col']` | Select by label |
| `df.iloc[row_index, col_index]` | Select by index |
| `df[df['Age'] > 30]` | Filter rows by condition |

---

## 🔹 Cleaning Data
| Function | Description |
|-----------|--------------|
| `df.dropna()` | Remove rows with missing values |
| `df.fillna(value)` | Replace missing values |
| `df.drop(columns=['col'])` | Drop specific column(s) |
| `df.rename(columns={'old':'new'})` | Rename columns |
| `df.duplicated()` | Check for duplicate rows |
| `df.drop_duplicates()` | Remove duplicate rows |
| `df['col'].str.lower()` | Convert text to lowercase |
| `df['col'].astype(int)` | Change column type |

---

## 🔹 Aggregation & Grouping
| Function | Description |
|-----------|--------------|
| `df.groupby('col').mean()` | Average by group |
| `df['col'].value_counts()` | Count unique values |
| `df.sort_values('col')` | Sort by column |
| `df.pivot_table(values='A', index='B', columns='C')` | Create pivot table |

---

## 🔹 Visualization (built-in)
| Function | Description |
|-----------|--------------|
| `df['col'].plot(kind='hist')` | Histogram |
| `df['col'].value_counts().plot(kind='bar')` | Bar chart |
| `df.plot(kind='scatter', x='col1', y='col2')` | Scatter plot |

---

## 🔹 Exporting Results
| Function | Description |
|-----------|--------------|
| `df.to_csv("cleaned.csv", index=False)` | Export cleaned data |
| `df.to_excel("output.xlsx")` | Export to Excel |
| `df.to_json("output.json")` | Export to JSON |
