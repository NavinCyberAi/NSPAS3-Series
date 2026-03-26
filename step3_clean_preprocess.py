import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# load dataset
df = pd.read_csv("synthetic_dataset.csv")

print("Before cleaning:", df.shape)

# remove duplicates
df = df.drop_duplicates()

# remove missing values
df = df.dropna()

print("After cleaning:", df.shape)

# normalization
scaler = MinMaxScaler()

df[["Pressure_kPa","Voltage_V"]] = scaler.fit_transform(
df[["Pressure_kPa","Voltage_V"]]
)

# save cleaned dataset
df.to_csv("clean_dataset.csv", index=False)

print("Clean dataset saved")
print(df.head())