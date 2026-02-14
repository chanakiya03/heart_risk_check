# import joblib
# import os
# import numpy as np
# import pandas as pd

# # ======================================================
# # PATHS
# # ======================================================
# CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# MODEL_PATH = os.path.join(CURRENT_DIR, "model.pkl")
# FEATURES_PATH = os.path.join(CURRENT_DIR, "features.pkl")

# # ======================================================
# # PREDICT FUNCTION
# # ======================================================
# def predict_risk(input_data):
#     """
#     input_data -> dict or DataFrame of features
#     returns -> (percentage, level)
#     """

#     # 1. Safety Checks
#     if not os.path.exists(MODEL_PATH) or not os.path.exists(FEATURES_PATH):
#         raise FileNotFoundError("Model or Features not found. Run train.py first.")

#     # 2. Load Model & Feature Names
#     model = joblib.load(MODEL_PATH)
#     feature_names = joblib.load(FEATURES_PATH)

#     # 3. Align Input Data with Training Features
#     # This ensures 'age' goes to 'age', 'sex' to 'sex', etc., regardless of dict order
#     try:
#         # Convert dict to DataFrame if it isn't one already
#         if isinstance(input_data, dict):
#             input_df = pd.DataFrame([input_data])
#         else:
#             input_df = input_data

#         # Reorder columns to match training data exactly
#         input_df = input_df[feature_names]
        
#     except KeyError as e:
#         raise ValueError(f"Missing feature in input data: {e}")

#     # 4. Predict
#     # [0][1] gives the probability of class '1' (Heart Disease)
#     prob = model.predict_proba(input_df)[0][1]
#     percent = round(float(prob) * 100, 2)

#     # 5. Determine Level
#     if percent < 30:
#         level = "Low"
#     elif percent < 70:
#         level = "Medium"
#     else:
#         level = "High"

#     return percent, level




# import joblib
# import os
# import pandas as pd
# import numpy as np

# ARTIFACT_PATH = os.path.dirname(os.path.abspath(__file__))

# def predict_risk(data_dict):
#     # Load Artifacts
#     model = joblib.load(os.path.join(ARTIFACT_PATH, 'model.pkl'))
#     scaler = joblib.load(os.path.join(ARTIFACT_PATH, 'scaler.pkl'))
#     features = joblib.load(os.path.join(ARTIFACT_PATH, 'features.pkl'))

#     # Prepare DataFrame
#     df = pd.DataFrame([data_dict])
    
#     # Ensure columns order matches training
#     df = df[features]
    
#     # Scale & Predict
#     scaled_data = scaler.transform(df)
#     prob = model.predict_proba(scaled_data)[0][1] # Probability of '1' (Disease)
    
#     percent = round(prob * 100, 2)
#     level = "High" if percent > 70 else "Medium" if percent > 30 else "Low"
    
#     return percent, level


import os
import joblib
import pandas as pd
import numpy as np

# Define artifact path (adjust if needed)
ARTIFACT_PATH = os.path.dirname(os.path.abspath(__file__))

# Load artifacts once at startup
MODEL_PATH = os.path.join(ARTIFACT_PATH, 'model.pkl')
SCALER_PATH = os.path.join(ARTIFACT_PATH, 'scaler.pkl')
FEATURES_PATH = os.path.join(ARTIFACT_PATH, 'features.pkl')

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    features = joblib.load(FEATURES_PATH)
except Exception as e:
    raise Exception(f"Error loading artifacts: {e}")


def predict_risk(data_dict):
    """
    Predict heart disease risk.

    Args:
        data_dict (dict): Patient data with keys matching training features.

    Returns:
        tuple: (percent risk, risk level as 'Low', 'Medium', 'High')
    """
    # Convert to DataFrame
    df = pd.DataFrame([data_dict])
    
    # Check for missing features
    missing_cols = [col for col in features if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing features: {missing_cols}")

    # Extra columns are ignored
    df = df[features]
    
    # Scale the data
    scaled_data = scaler.transform(df)
    
    # Predict probability
    prob = model.predict_proba(scaled_data)[0][1]  # Probability of '1' (Disease)
    
    # Convert to percentage
    percent = round(prob * 100, 2)
    
    # Determine risk level
    if percent > 70:
        level = "High"
    elif percent > 30:
        level = "Medium"
    else:
        level = "Low"
    
    return percent, level


# Example usage
if __name__ == "__main__":
    sample_patient = {
        "age": 63,
        "sex": 1,
        "cp": 3,
        "trestbps": 145,
        "chol": 233,
        "fbs": 1,
        "restecg": 0,
        "thalach": 150,
        "exang": 0,
        "oldpeak": 2.3,
        "slope": 1,
        "ca": 0,
        "thal": 2
    }

    risk_percent, risk_level = predict_risk(sample_patient)
    print(f"Heart Disease Risk: {risk_percent}% ({risk_level})")
