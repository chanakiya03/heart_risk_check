import pandas as pd
import joblib
import os
from api.models import Patient
from sklearn.ensemble import RandomForestClassifier

# Paths consistent with train.py
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "heart.csv")

MODEL_PATH = os.path.join(CURRENT_DIR, "model.pkl")
FEATURES_PATH = os.path.join(CURRENT_DIR, "features.pkl")

def retrain_model_logic():
    # Load initial dataset
    if os.path.exists(DATASET_PATH):
        csv_data = pd.read_csv(DATASET_PATH)
    else:
        csv_data = pd.DataFrame()

    # Get new data from DB
    patients = Patient.objects.exclude(target=None).values()
    db_data = pd.DataFrame(list(patients))

    if not db_data.empty:
        # Clean db_data to match heart.csv structure
        cols_to_keep = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"]
        db_data = db_data[cols_to_keep]
        
        if not csv_data.empty:
            data = pd.concat([csv_data, db_data], ignore_index=True)
        else:
            data = db_data
    else:
        data = csv_data

    if data.empty:
        print("No data available for training.")
        return

    X = data.drop(columns=["target"])
    y = data["target"]
    feature_names = list(X.columns)

    # Updated parameters from train.py
    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=8,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    )
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(feature_names, FEATURES_PATH)
    
    print("Model retrained successfully and saved.")
