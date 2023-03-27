from rest_framework import serializers
from .models import *

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['TargetName'] 

class DrugSerializer(serializers.ModelSerializer):
    targets_for_drug = TargetSerializer(many=True)

    class Meta:
        model = Drug
        exclude = ['id', 'Diseases', 'DrugID']

class DrugSMILSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        exclude = ['id', 'Diseases', 'DrugID']           


class DiseaseSerializer(serializers.ModelSerializer):
    targets_for_disease = TargetSerializer(many=True)
    drugs_for_disease = DrugSerializer(many=True)

    class Meta:
        model = Disease
        exclude = ['id', 'DiseaseID']

# class DiseaseSerializerForSMIL(serializers.ModelSerializer):
#     # targets_for_disease = TargetSerializer(many=True)
#     drugs_for_disease = DrugSerializer(many=True)

#     class Meta:
#         model = Disease
#         exclude = ['id', 'DiseaseID']        
