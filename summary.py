
# Import Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

data_piece = "Low"

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, axs = plt.subplots(1, 1)

axs.axis('tight')
axs.axis('off')

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

columns = ["Date", "Close", "Low", "High"]
df = pd.read_csv("data.csv", usecols=columns)

# Plot
dfs = []
bottoms = []
highs = []

quarters = ["Q1", "Q2", "Q3", "Q4"]
table_cols = ["n", "mean", "sd", "min", "median", "max"]

for i,h in enumerate(df.High):
    highs.append(h-df.Low[i])

for p in points:
    dfs.append(getattr(df, p))

data = []

quarter = int(len(df.Date) / 4)

for i in range(0, len(df.Date), quarter):
    index = len(data)

    d = [df[data_piece][i] for i in range(i, quarter + i)]

    _n = quarter
    _mean = round(sum(d) / quarter, 2)
    _min = min(d)
    _median = statistics.median(d)
    _max = max(d)
    _sd = round(np.std(d), 2)

    data.append([_n, _mean, _sd, _min, _median, _max])

axs.table(rowLabels=quarters, colLabels=table_cols, cellText=data, loc="center")

# Add title

plt.title("Plot without limiting axes")

# Display

plt.show()