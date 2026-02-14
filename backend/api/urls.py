# from django.urls import path
# from .views import predict_patient, retrain_model, patient_history

# urlpatterns = [
#     path("predict/", predict_patient, name="predict-patient"),
#     path("retrain/", retrain_model, name="retrain-model"),
#     path("history/", patient_history, name="patient-history"),
# ]




from django.urls import path
from .views import predict_view # Change import
from .views import retrain_model


urlpatterns = [
    path('predict/', predict_view, name='predict_patient'), # Change view usage
    path('retrain/', retrain_model, name='retrain_model'),
]
