# from django.db import models


# class Patient(models.Model):

#     SEX_CHOICES = [(0, "Female"), (1, "Male")]

#     CP_CHOICES = [
#         (0, "Typical Angina"),
#         (1, "Atypical Angina"),
#         (2, "Non-anginal Pain"),
#         (3, "Asymptomatic"),
#     ]

#     SLOPE_CHOICES = [(0, "Upsloping"), (1, "Flat"), (2, "Downsloping")]

#     THAL_CHOICES = [(1, "Normal"), (2, "Fixed Defect"), (3, "Reversable Defect")]

#     age = models.IntegerField()
#     sex = models.IntegerField(choices=SEX_CHOICES)
#     cp = models.IntegerField(choices=CP_CHOICES)

#     trestbps = models.FloatField()
#     chol = models.FloatField()

#     fbs = models.IntegerField()
#     restecg = models.IntegerField()
#     thalach = models.FloatField()
#     exang = models.IntegerField()

#     oldpeak = models.FloatField()
#     slope = models.IntegerField(choices=SLOPE_CHOICES)
#     ca = models.IntegerField()
#     thal = models.IntegerField(choices=THAL_CHOICES)

#     risk_percentage = models.FloatField(null=True, blank=True)
#     risk_level = models.CharField(max_length=10, null=True, blank=True)

#     target = models.IntegerField(null=True, blank=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.id} → {self.risk_percentage}%"

from django.db import models

class Patient(models.Model):
    # --- Choices for Categorical Data ---
    SEX_CHOICES = [(0, "Female"), (1, "Male")]
    CP_CHOICES = [
        (0, "Typical Angina"), (1, "Atypical Angina"), 
        (2, "Non-anginal Pain"), (3, "Asymptomatic")
    ]
    # (Add other choices as needed for UI, storing as Int is fine for ML)

    # --- Input Features (13 Total) ---
    age = models.IntegerField()
    sex = models.IntegerField(choices=SEX_CHOICES)
    cp = models.IntegerField(choices=CP_CHOICES)
    trestbps = models.FloatField()
    chol = models.FloatField()
    fbs = models.IntegerField()  # 1=True, 0=False
    restecg = models.IntegerField()
    thalach = models.FloatField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()

    # --- Prediction Results ---
    risk_percentage = models.FloatField(null=True, blank=True)
    risk_level = models.CharField(max_length=20, null=True, blank=True)
    
    # --- Actual Diagnosis (For Retraining) ---
    target = models.IntegerField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patient {self.id} | Risk: {self.risk_level}"