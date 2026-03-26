import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("synthetic_dataset.csv")

# show dataset information
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset statistics:")
print(df.describe())

# Histogram of pressure
plt.figure()
sns.histplot(df["Pressure_kPa"], bins=30)
plt.title("Pressure Distribution")
plt.xlabel("Pressure_kPa")
plt.ylabel("Count")
plt.savefig("pressure_histogram.png")
plt.show()

# Scatter plot pressure vs voltage
plt.figure()
sns.scatterplot(x=df["Pressure_kPa"], y=df["Voltage_V"])
plt.title("Pressure vs Voltage")
plt.xlabel("Pressure_kPa")
plt.ylabel("Voltage_V")
plt.savefig("pressure_voltage_scatter.png")
plt.show()