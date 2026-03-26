import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("feature_dataset.csv")

# create balanced label
threshold = df["Voltage_V"].median()
df["label"] = (df["Voltage_V"] > threshold).astype(int)

X = df[["Pressure_kPa","Voltage_V","pressure_change","voltage_change"]]
y = df["label"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test,pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test,pred))
print("\nClassification Report:\n", classification_report(y_test,pred))