import csv

# Open the dataset
with open("screen_addiction_risk_dataset.csv", "r") as file:

    reader = csv.DictReader(file)

    data = list(reader)

# Display the first five records
print("First five records:")

for row in data[:5]:
    print(row)

# Display total records
print("\nTotal records:", len(data))


# Separate input features and target

feature_names = [
    "Daily_Screen_Time",
    "Social_Media_Hours",
    "Gaming_Hours",
    "Sleep_Hours",
    "Phone_Pickups",
    "Study_Work_Hours",
    "Notifications"
]

X = []
y = []

for row in data:

    features = [
        float(row[name]) for name in feature_names
    ]

    X.append(features)

    y.append(row["Risk_Level"])

print("\nInput Features (X):")
print(X[:5])

print("\nTarget Values (y):")
print(y[:5])


from sklearn.model_selection import train_test_split

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Display dataset sizes
print("Training data:", len(X_train))
print("Testing data:", len(X_test))

print("Training labels:", len(y_train))
print("Testing labels:", len(y_test))



from sklearn.ensemble import RandomForestClassifier

# Create the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")


from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Make predictions
y_pred = model.predict(X_test)



# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy * 100, "%")

# Display confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

import pickle

# Save the trained model
with open("screen_addiction_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")

