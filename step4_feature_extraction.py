import pandas as pd

df = pd.read_csv("clean_dataset.csv")

# create new features
df["pressure_change"] = df["Pressure_kPa"].diff()
df["voltage_change"] = df["Voltage_V"].diff()

df.fillna(0, inplace=True)

df.to_csv("feature_dataset.csv", index=False)

print("Feature dataset created")
print(df.head())