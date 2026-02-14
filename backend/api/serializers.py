# from rest_framework import serializers
# from .models import Patient

# class PatientInputSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Patient
#         # Ensure we capture all inputs needed for prediction
#         exclude = ["risk_percentage", "risk_level", "target", "created_at"]

# class PatientOutputSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Patient
#         fields = "__all__"  # Return everything including the ID

# class PatientDiagnosisSerializer(serializers.ModelSerializer):
#     """Serializer for updating the actual medical result later"""
#     class Meta:
#         model = Patient
#         fields = ["target"]
#         extra_kwargs = {'target': {'required': True}}


from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['risk_percentage', 'risk_level', 'target']