import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("feature_dataset.csv")

# create fault label
df["label"] = ((df["Voltage_V"] < 1.0) | (df["Voltage_V"] > 4.0)).astype(int)

X = df[["Pressure_kPa","Voltage_V","pressure_change","voltage_change"]]
y = df["label"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()

model.fit(X_train,y_train)

print("Model trained successfully")