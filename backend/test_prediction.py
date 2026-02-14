import joblib
import os
import numpy as np

MODEL_PATH = r"d:\projects\heart\backend\api\ml\model.pkl"

def test_user_case():
    if not os.path.exists(MODEL_PATH):
        print("Model file not found!")
        return

    model = joblib.load(MODEL_PATH)
    
    # User's data:
    # Age: 35, Sex: 1, CP: 1, BP: 190, Chol: 211, FBS: 1, ECG: 1, HR: 120, Angina: 1, Oldpeak: 1.2, Slope: 1, Vessels: 1, Thal: 2
    # Features order in train.py: X = data.drop("target", axis=1)
    # Expected heart.csv order (standard): age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
    features = [35.0, 1.0, 1.0, 190.0, 211.0, 1.0, 1.0, 120.0, 1.0, 1.2, 1.0, 1.0, 2.0]
    
    prob = model.predict_proba([features])[0][1]
    percent = round(float(prob) * 100, 2)
    
    if percent < 30:
        level = "Low"
    elif percent < 70:
        level = "Medium"
    else:
        level = "High"
        
    print(f"User Case Data: {features}")
    print(f"Prediction Result: {percent}% ({level} Risk)")

if __name__ == "__main__":
    test_user_case()
