# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404

# from .models import Patient
# from .serializers import (
#     PatientInputSerializer, 
#     PatientOutputSerializer, 
#     PatientDiagnosisSerializer
# )
# from .ml.predict import predict_risk
# from .ml.retrain import retrain_model_logic

# # =================================================
# # Predict
# # =================================================
# @api_view(["POST"])
# def predict_patient(request):
#     serializer = PatientInputSerializer(data=request.data)

#     if not serializer.is_valid():
#         return Response(serializer.errors, status=400)

#     # Get validated dict
#     data = serializer.validated_data

#     try:
#         # Pass the dictionary directly; predict.py handles the ordering
#         percent, level = predict_risk(data)
        
#         # Save to DB
#         patient = serializer.save(
#             risk_percentage=percent, 
#             risk_level=level
#         )

#         return Response(PatientOutputSerializer(patient).data, status=201)
    
#     except Exception as e:
#         return Response({"error": str(e)}, status=500)

# # =================================================
# # Update Diagnosis (Feedback Loop)
# # =================================================
# @api_view(["PATCH"])
# def update_diagnosis(request, pk):
#     """
#     Allows a doctor to update the 'target' field (0 or 1) 
#     after the actual medical diagnosis is confirmed.
#     """
#     patient = get_object_or_404(Patient, pk=pk)
#     serializer = PatientDiagnosisSerializer(patient, data=request.data, partial=True)

#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Diagnosis updated successfully"})
    
#     return Response(serializer.errors, status=400)

# # =================================================
# # Retrain
# # =================================================
# @api_view(["POST"])
# def retrain_model(request):
#     try:
#         msg = retrain_model_logic()
#         return Response({"message": msg})
#     except Exception as e:
#         return Response({"error": str(e)}, status=500)

# # =================================================
# # History
# # =================================================
# @api_view(["GET"])
# def patient_history(request):
#     # This was where your error was:
#     patients = Patient.objects.all().order_by('-created_at')[:50]
#     return Response(PatientOutputSerializer(patients, many=True).data)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatientSerializer
from .ml.predict import predict_risk
from django.http import JsonResponse
from .ml.train import train_model  # import your training function

@api_view(['POST'])
def predict_view(request):
    serializer = PatientSerializer(data=request.data)
    
    if serializer.is_valid():
        # Get prediction
        try:
            percent, level = predict_risk(serializer.validated_data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

        # Save to DB
        serializer.save(risk_percentage=percent, risk_level=level)
        
        # Return result
        return Response({
            "risk_percentage": percent,
            "risk_level": level,
            "data": serializer.data
        })
        
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def retrain_model(request):
    try:
        train_model()  # retrain the model
        return JsonResponse({'status': 'success', 'message': 'Model retrained successfully!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)