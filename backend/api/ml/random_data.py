import pandas as pd
import numpy as np

# Number of rows you want
N = 600000
# Seed for reproducibility
np.random.seed(42)

# Feature distributions based on your example data
age = np.random.randint(29, 77, N)  # realistic age range
sex = np.random.choice([0, 1], N)   # 0=female, 1=male
cp = np.random.choice([0,1,2,3], N, p=[0.2,0.25,0.25,0.3])
trestbps = np.random.randint(100, 200, N)
chol = np.random.randint(126, 564, N)
fbs = np.random.choice([0,1], N, p=[0.7,0.3])
restecg = np.random.choice([0,1,2], N, p=[0.6,0.3,0.1])
thalach = np.random.randint(96, 202, N)
exang = np.random.choice([0,1], N, p=[0.7,0.3])
oldpeak = np.round(np.random.uniform(0, 6.2, N), 1)
slope = np.random.choice([0,1,2], N, p=[0.1,0.4,0.5])
ca = np.random.choice([0,1,2,3,4], N, p=[0.5,0.2,0.2,0.05,0.05])
thal = np.random.choice([0,1,2,3], N, p=[0.1,0.1,0.3,0.5])
# Target: 1=Heart disease, 0=No heart disease (approx 55% disease)
target = np.random.choice([0,1], N, p=[0.45,0.55])

# Create DataFrame
df = pd.DataFrame({
    'age': age,
    'sex': sex,
    'cp': cp,
    'trestbps': trestbps,
    'chol': chol,
    'fbs': fbs,
    'restecg': restecg,
    'thalach': thalach,
    'exang': exang,
    'oldpeak': oldpeak,
    'slope': slope,
    'ca': ca,
    'thal': thal,
    'target': target
})

# Optional: shuffle rows
df = df.sample(frac=1).reset_index(drop=True)

# Save to CSV
df.to_csv("synthetic_heart_disease_600.csv", index=False)
print("✅ Synthetic dataset with 600 rows generated!")
print(df.head())
