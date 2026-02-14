# import pandas as pd
# import joblib
# import os

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score


# # ======================================================
# # PATH SETUP
# # ======================================================

# CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))  # go to backend

# DATASET_PATH = os.path.join(BASE_DIR, "dataset", "heart.csv")

# MODEL_PATH = os.path.join(CURRENT_DIR, "model.pkl")
# FEATURES_PATH = os.path.join(CURRENT_DIR, "features.pkl")


# # ======================================================
# # TRAIN FUNCTION
# # ======================================================

# def train_initial_model():

#     print("📂 Loading dataset from:", DATASET_PATH)

#     if not os.path.exists(DATASET_PATH):
#         raise FileNotFoundError("❌ heart.csv not found in backend/dataset/")

#     df = pd.read_csv(DATASET_PATH)

#     # -------------------------
#     # Split features + target
#     # -------------------------
#     X = df.drop(columns=["target"])
#     y = df["target"]

#     feature_names = list(X.columns)

#     # -------------------------
#     # Train / Test split
#     # -------------------------
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y,
#         test_size=0.2,
#         random_state=42,
#         stratify=y
#     )

#     # -------------------------
#     # RandomForest (BEST for heart dataset)
#     # -------------------------
#     model = RandomForestClassifier(
#         n_estimators=500,
#         max_depth=8,
#         class_weight="balanced",
#         random_state=42,
#         n_jobs=-1
#     )

#     model.fit(X_train, y_train)

#     # -------------------------
#     # Evaluate
#     # -------------------------
#     preds = model.predict(X_test)
#     acc = accuracy_score(y_test, preds)

#     print(f"✅ Accuracy: {acc * 100:.2f}%")

#     # -------------------------
#     # Save model
#     # -------------------------
#     joblib.dump(model, MODEL_PATH)
#     joblib.dump(feature_names, FEATURES_PATH)

#     print("💾 model.pkl saved")
#     print("💾 features.pkl saved")
#     print("🎉 Training complete!")


# # ======================================================
# # RUN
# # ======================================================

# if __name__ == "__main__":
#     train_initial_model()



# import pandas as pd
# import joblib
# import os
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split

# # Paths
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# DATA_PATH = os.path.join(BASE_DIR, 'dataset', 'heart.csv')
# ARTIFACT_PATH = os.path.dirname(os.path.abspath(__file__))

# def train():
#     if not os.path.exists(DATA_PATH):
#         print("❌ Dataset not found!")
#         return

#     df = pd.read_csv(DATA_PATH)
#     X = df.drop('target', axis=1)
#     y = df['target']

#     # Scaling
#     scaler = StandardScaler()
#     X_scaled = scaler.fit_transform(X)

#     # Model
#     model = RandomForestClassifier(n_estimators=100, random_state=42)
#     model.fit(X_scaled, y)

#     # Save Artifacts
#     joblib.dump(model, os.path.join(ARTIFACT_PATH, 'model.pkl'))
#     joblib.dump(scaler, os.path.join(ARTIFACT_PATH, 'scaler.pkl'))
#     joblib.dump(list(X.columns), os.path.join(ARTIFACT_PATH, 'features.pkl'))
#     print("✅ Model trained and saved.")

# if __name__ == "__main__":
#     train()






# import pandas as pd
# import joblib
# import os
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler

# # ==========================================
# # PATH SETUP
# # ==========================================
# # Current script location: D:\projects\heart\backend\api\ml\train.py
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # Dataset is in: D:\projects\heart\backend\dataset\heart.csv
# DATA_PATH = os.path.join(BASE_DIR, 'dataset', 'heart.csv')
# # Save artifacts directly in the ml folder
# ARTIFACT_PATH = os.path.dirname(os.path.abspath(__file__))  # ml folder

# def train_model():
#     print(f"📂 Loading dataset from: {DATA_PATH}")

#     if not os.path.exists(DATA_PATH):
#         print("❌ Error: heart.csv not found!")
#         return

#     # Load dataset
#     df = pd.read_csv(DATA_PATH)

#     # ==========================================
#     # FIX TARGET: 1 = Risk, 0 = Healthy
#     # ==========================================
#     df['target'] = 1 - df['target']
#     print("✅ Target flipped: 1 = Risk, 0 = Healthy")

#     # Split features and target
#     X = df.drop('target', axis=1)
#     y = df['target']

#     # ==========================================
#     # SCALE FEATURES
#     # ==========================================
#     scaler = StandardScaler()
#     X_scaled = scaler.fit_transform(X)
#     print("✅ Features scaled")

#     # ==========================================
#     # TRAIN RANDOM FOREST MODEL
#     # ==========================================
#     model = RandomForestClassifier(n_estimators=100, random_state=42)
#     model.fit(X_scaled, y)
#     print("✅ Random Forest model trained")

#     # ==========================================
#     # SAVE ARTIFACTS DIRECTLY IN ML FOLDER
#     # ==========================================
#     joblib.dump(model, os.path.join(ARTIFACT_PATH, 'model.pkl'))
#     joblib.dump(scaler, os.path.join(ARTIFACT_PATH, 'scaler.pkl'))
#     joblib.dump(list(X.columns), os.path.join(ARTIFACT_PATH, 'features.pkl'))
#     print(f"✅ Model, scaler, and features saved directly in: {ARTIFACT_PATH}")


# if __name__ == "__main__":
#     train_model()




import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==========================================
# PATH SETUP
# ==========================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, 'dataset', 'heart.csv')
ARTIFACT_PATH = os.path.dirname(os.path.abspath(__file__))  # Save artifacts in ml folder

def train_model(test_size=0.2, random_state=42):
    """
    Train Random Forest on heart disease dataset and save artifacts.

    Args:
        test_size (float): Fraction of dataset for testing
        random_state (int): Random seed
    """
    print(f"📂 Loading dataset from: {DATA_PATH}")

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"❌ Dataset not found at {DATA_PATH}")

    # Load dataset
    df = pd.read_csv(DATA_PATH)
    print(f"✅ Dataset loaded: {df.shape[0]} records, {df.shape[1]} columns")

    # ==========================================
    # FIX TARGET: 1 = Risk, 0 = Healthy
    # ==========================================
    if df['target'].max() == 1 and df['target'].min() == 0:
        df['target'] = 1 - df['target']  # Flip 1=Risk, 0=Healthy
        print("✅ Target flipped: 1 = Risk, 0 = Healthy")
    else:
        print("ℹ️ Target column already matches convention")

    # Split features and target
    X = df.drop('target', axis=1)
    y = df['target']

    # ==========================================
    # SCALE FEATURES
    # ==========================================
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("✅ Features scaled")

    # ==========================================
    # SPLIT DATA FOR TRAIN/TEST
    # ==========================================
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=test_size, random_state=random_state, stratify=y
    )
    print(f"✅ Data split: {len(X_train)} train, {len(X_test)} test")

    # ==========================================
    # TRAIN RANDOM FOREST MODEL
    # ==========================================
    model = RandomForestClassifier(n_estimators=100, random_state=random_state)
    model.fit(X_train, y_train)
    print("✅ Random Forest model trained")

    # Evaluate on test set
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"📊 Test Accuracy: {acc*100:.2f}%")

    # ==========================================
    # SAVE ARTIFACTS
    # ==========================================
    os.makedirs(ARTIFACT_PATH, exist_ok=True)
    joblib.dump(model, os.path.join(ARTIFACT_PATH, 'model.pkl'))
    joblib.dump(scaler, os.path.join(ARTIFACT_PATH, 'scaler.pkl'))
    joblib.dump(list(X.columns), os.path.join(ARTIFACT_PATH, 'features.pkl'))
    print(f"✅ Model, scaler, and features saved in: {ARTIFACT_PATH}")


if __name__ == "__main__":
    train_model()

