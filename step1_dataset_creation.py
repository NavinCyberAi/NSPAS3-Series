import pandas as pd
import numpy as np

# Load original dataset
df = pd.read_csv("Nspas3_original.csv")

print("Original dataset shape:", df.shape)
print(df.head())

# Generate synthetic pressure values (2000 rows)
pressure = np.random.uniform(10, 115, 2000)

# Sensor constants
A = 0.008095
B = -0.000952
VDD = 5

# Calculate voltage
voltage = (A * pressure + B) * VDD

# Add small noise to make it realistic
noise = np.random.normal(0, 0.05, 2000)
voltage = voltage + noise

# Create synthetic dataset
synthetic_df = pd.DataFrame({
    "Pressure_kPa": pressure,
    "Voltage_V": voltage
})

# Save new dataset
synthetic_df.to_csv("synthetic_dataset.csv", index=False)

print("\nSynthetic dataset created successfully")
print("Synthetic dataset shape:", synthetic_df.shape)
print(synthetic_df.head())