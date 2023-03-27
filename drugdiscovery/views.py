from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import pandas as pd


# Creating views here.
@api_view(["GET"])
def get_all_disease(request, disease_name):
    # print(disease_name)
    if request.method == "GET":
        try:
            disease = Disease.objects.get(DiseaseName=disease_name)
            serializedData = DiseaseSerializer(disease)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializedData.data)
    
@api_view(["GET"])
def get_all_smil(request, disease_name):
    # print(disease_name)
    if request.method == "GET":
        try:
            disease = Disease.objects.get(DiseaseName=disease_name)
            # print(disease)
            drugs = disease.drugs_for_disease.exclude(DrugSMIL = 'default_value')
            drugs = drugs.filter(ClinicalStatus = 'Phase 3')[0:5]
            # print(drugs)
            serializedData = DrugSMILSerializer(drugs, many=True)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializedData.data)    

@api_view(["GET"])
def get_all_drugs(request, drug_name):
    # print(drug_name)
    if request.method == "GET":
        try:
            drug = Drug.objects.get(DrugName=drug_name)
            serializedData = DiseaseSerializer(drug)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializedData.data)




@api_view(["GET"])
def create_database(request):
    # df = pd.read_excel('DrugXDiseaseMapping.xlsx')

    disease_id = "234"
    disease_name = "aml"

    drug_id = "567"
    drug_name = "ALD"
    clinical_status = "Phase-1"

    target_id = "789"
    target_name = "DNA TOPO"

    df = pd.read_excel('DrugXDiseaseMapping.xlsx')
    df2 = pd.read_excel('TargetXDrug.xlsx')
    df3 = pd.read_excel('TargetIDXTargetName.xlsx')

    # df = pd.DataFrame(df, columns=['DrugUID', 'DrugName', 
    #                                  'DiseaseName', 'DiseaseID', "ClinicalStatus"])

    Drugs = []
    Targets = []
    i=0
    for ind in df.index:
            i+=1
            print(i)
            DrugUID = df['DrugUID'][ind]
            for ind2 in df2.index:
                # print(DrugUID)
                if df2['DrugID'][ind2] == DrugUID:
                    for ind3 in df3.index:

                        if df3['TargetID'][ind3] == df2['TargetID'][ind2]:

                            DrugUID = df['DrugUID'][ind]
                            # print("DiseaseName:", df['DiseaseName'][ind], "\tDrugUID:", df['DrugUID'][ind], "\tDrugName:", df['DrugName'][ind])
                            # print("TargetName:", df3['TargetName'][ind3])

                            disease_id = df['DiseaseID'][ind]
                            disease_name = df['DiseaseName'][ind]

                            drug_id = df['DrugUID'][ind]
                            drug_name = df['DrugName'][ind]
                            clinical_status = df['ClinicalStatus'][ind]

                            target_id = df2['TargetID'][ind2]
                            target_name = df3['TargetName'][ind3]



                            try:
                                temp_d = Disease.objects.get(DiseaseID = disease_id)
                            except:
                                temp_d = Disease(DiseaseID=disease_id, DiseaseName=disease_name)
                                temp_d.save()

                            # print(temp_d)    

                            try:
                                temp_drug = Drug.objects.get(DrugID = drug_id)
                            except:
                                temp_drug = Drug(DrugID=drug_id, DrugName=drug_name,ClinicalStatus= clinical_status)
                                temp_drug.save()  
                                temp_drug.Diseases.add(temp_d)

                            # print(temp_drug)    

                            try:
                                temp_t = Target.objects.get(TargetID = target_id)
                            except:
                                temp_t = Target(TargetID=target_id, TargetName=target_name)
                                temp_t.save()
                                temp_t.Diseases.add(temp_d)
                                temp_t.Drugs.add(temp_drug)

    if request.method == "GET":

        return Response(status=status.HTTP_201_CREATED)        

# @api_view(["POST"])
# def post_disease(request):
#     # print("Posting")
#     if request.method == "POST":
#         # print("Posting23")
#         serialized_bloodtest_data = BloodTestSerializer(data=request.data)
        
#         if serialized_bloodtest_data.is_valid():
#             serialized_bloodtest_data.save()

#             return Response(status=status.HTTP_201_CREATED)
#         return Response(
#             serialized_bloodtest_data.errors, status=status.HTTP_400_BAD_REQUEST
#         )

# @api_view(["POST"])
# def post_bloodtest_data(request):
#     # print("Posting")
#     if request.method == "POST":
#         # print("Posting23")
#         serialized_bloodtest_data = BloodTestSerializer(data=request.data)
        
#         if serialized_bloodtest_data.is_valid():
#             serialized_bloodtest_data.save()

#             return Response(status=status.HTTP_201_CREATED)
#         return Response(
#             serialized_bloodtest_data.errors, status=status.HTTP_400_BAD_REQUEST
#         )



# @api_view(["GET"])
# def get_bloodtest_data(request):
#     if request.method == "GET":
#         bloodtest_data = BloodTestData.objects.all()
#         serializedData = BloodTestSerializer(bloodtest_data, many=True)
#         return Response(serializedData.data)
        

@api_view(["GET"])
def push_smil(request):

    df = pd.read_excel('23.xlsx')

    for ind in df.index:
        drug_id = df['DrugUID'][ind]
        drug_smil = df['DrugSMIL'][ind]

        try:
            drug = Drug.objects.get(DrugID=drug_id)
        except:
            continue

        drug.DrugSMIL = drug_smil
        drug.save()
        # print(drug_id, drug.DrugID, drug.DrugName, drug.DrugSMIL, drug_smil)




    if request.method == "GET":
        return Response(status=status.HTTP_201_CREATED)
    