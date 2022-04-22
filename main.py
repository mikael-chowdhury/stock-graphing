# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

points = ["Close", "Low"]

# Define Data

columns = ["Date", *points]
df = pd.read_csv("data.csv", usecols=columns)

# Plot

for point in points:
    plt.plot(df.Date, getattr(df, point), label=point)

# Add title

plt.title("Plot without limiting axes")

# Add labels

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.ylim([6000, 8000])

# Display

plt.legend()
plt.show()