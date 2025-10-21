
---

# 🎨 Matplotlib Cheatsheet

---

## 🧩 1. Setup

```python
import matplotlib.pyplot as plt
%matplotlib inline  # (Jupyter/Colab only)
```

---

## 📊 2. Basic Plots

| Type               | Code                                                | Description                 |
| ------------------ | --------------------------------------------------- | --------------------------- |
| **Line plot**      | `plt.plot(x, y)`                                    | Connect points with lines   |
| **Scatter plot**   | `plt.scatter(x, y)`                                 | Individual points           |
| **Bar chart**      | `plt.bar(categories, values)`                       | Vertical bars               |
| **Horizontal bar** | `plt.barh(categories, values)`                      | Horizontal bars             |
| **Histogram**      | `plt.hist(data, bins=10)`                           | Distribution of values      |
| **Box plot**       | `plt.boxplot(data)`                                 | Median, quartiles, outliers |
| **Pie chart**      | `plt.pie(values, labels=labels, autopct='%1.1f%%')` | Circular proportion chart   |

---

## 🧭 3. Labels, Titles & Legends

```python
plt.title("My Plot Title")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.legend(["Series 1", "Series 2"])
```

---

## 🎨 4. Colors, Styles & Markers

| Option       | Example                   | Effect                      |
| ------------ | ------------------------- | --------------------------- |
| Color        | `color='skyblue'`         | Sets color                  |
| Marker       | `marker='o'`              | Adds markers to line plot   |
| Line style   | `linestyle='--'`          | Dashed lines                |
| Combined     | `plt.plot(x, y, 'ro--')`  | Red, circle markers, dashed |
| Style preset | `plt.style.use('ggplot')` | Apply full visual theme     |

---

## 🧱 5. Multiple Plots

### ▶️ Multiple Lines in One Figure

```python
plt.plot(x, y1, label='Train')
plt.plot(x, y2, label='Test')
plt.legend()
plt.show()
```

### 🪞 Subplots (Side-by-Side)

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].hist(df['Age'], color='lightblue')
axs[0].set_title('Age Distribution')

axs[1].bar(df['Pclass'].value_counts().index,
           df['Pclass'].value_counts().values,
           color='salmon')
axs[1].set_title('Passenger Class Count')

plt.tight_layout()
plt.show()
```

---

## 🧠 6. Figure Control

| Command                          | Description                    |
| -------------------------------- | ------------------------------ |
| `plt.figure(figsize=(8, 5))`     | Set figure size                |
| `plt.subplot(rows, cols, index)` | Create multiple plots manually |
| `plt.tight_layout()`             | Prevent overlapping labels     |
| `plt.grid(True)`                 | Add gridlines                  |
| `plt.xlim(min, max)`             | Limit x-axis range             |
| `plt.ylim(min, max)`             | Limit y-axis range             |
| `plt.show()`                     | Display the figure             |

---

## 💾 7. Saving Plots

```python
plt.savefig("plot.png", dpi=300, bbox_inches='tight')
```

* `dpi` = image resolution (higher → better quality)
* `bbox_inches='tight'` trims white borders

---

## 🧩 8. Pandas Integration

Pandas plotting uses Matplotlib internally:

```python
df['Age'].hist()
df['Pclass'].value_counts().plot(kind='bar')
df.plot(kind='scatter', x='Age', y='Fare')
```

---

## 🧮 9. Quick Styling Reference

| Style   | Code                        | Description |
| ------- | --------------------------- | ----------- |
| `'b'`   | Blue line                   |             |
| `'g--'` | Green dashed line           |             |
| `'ro'`  | Red circles                 |             |
| `'k^'`  | Black triangles             |             |
| `'c*:'` | Cyan dotted line with stars |             |

---

## ✨ 10. Bonus: Color & Themes

```python
plt.style.available  # List of all built-in styles
plt.style.use('seaborn-v0_8-darkgrid')
```

---

💡 **Tip:**
Always call `plt.show()` after finishing your plot, especially in scripts or VS Code.
In notebooks, each cell can display one plot automatically.

---

Would you like me to make a **Pandas + Matplotlib combo cheatsheet next** (so you can see which plots are easiest to do directly from DataFrames)?
