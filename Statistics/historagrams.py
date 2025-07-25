import pandas as pd
import matplotlib.pyplot as plt


# Load data
heights = pd.read_csv("Statistics/height.csv")


# Plot histogram
fig, ax = plt.subplots()
plt.hist(heights['Height'], bins=6, edgecolor="black")
ax.set_xlabel('Height')
ax.set_ylabel('Frequency')


# plt.savefig('histogram6.png')
plt.show()

fig, ax = plt.subplots()

# # Plotting with more bins
# plt.hist(heights['Height'], bins=10)
# ax.set_xlabel('Height')
# ax.set_ylabel('Frequency')
# plt.show()