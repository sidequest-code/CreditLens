import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split

# Create directories if they don't exist
os.makedirs("models", exist_ok=True)

# Load data (ensure 'credit_data.csv' is inside a 'data' folder or same directory)
print("Loading dataset...")
df = pd.read_csv("credit_data.csv")

# Preprocessing
X = df.drop(columns=["default.payment.next.month", "ID"], errors="ignore")
y = df["default.payment.next.month"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train lightweight model
print("Training Random Forest risk model...")
model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
model.fit(X_train, y_train)

# Model Validation metrics (crucial for MRM)
auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
print(f"Model Validation Complete. Out-of-Sample ROC-AUC Score: {auc:.4f}")

# Save model artifact
with open("models/trained_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model artifact successfully saved to /models/trained_model.pkl")