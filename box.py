
# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

_min = 6000
_max = 8000

step = 50

major_step = 250

steps = []

_labels = []

for i in range(_min, _max, step):
    steps.append(i)

    if i % major_step == 0:
        _labels.append(i)
    else:
        _labels.append("")

points = ["Close", "Low", "High"]

# Define Data

columns = ["Date", *points]
df = pd.read_csv("data.csv", usecols=columns)

# Plot
dfs = []
bottoms = []
highs = []

for i,h in enumerate(df.High):
    highs.append(h-df.Low[i])

for p in points:
    dfs.append(getattr(df, p))

plt.bar(df.Date, highs, 0.5, df.Low, label="low-to-high")
plt.plot(df.Date, df.Close, color="red", label="close")

plt.grid(color='green', linestyle='-', linewidth=0.5, axis="y")

plt.yticks(steps, _labels)

# Add title

plt.title("box plot with y ticks")

# Add labels

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.ylim([_min, _max])

# Display

plt.legend()
plt.show()