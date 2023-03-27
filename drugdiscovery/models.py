from django.db import models

# Create your models here.

class Disease(models.Model):
    DiseaseID = models.CharField(max_length=120)
    DiseaseName = models.CharField(max_length=120)

    def _str_(self):
        return self.name

class Drug(models.Model):
    DrugID = models.CharField(max_length=120)
    DrugName = models.CharField(max_length=120)
    ClinicalStatus = models.CharField(max_length=120)
    DrugSMIL = models.CharField(max_length=500, default="default_value")
    Diseases = models.ManyToManyField(Disease, blank=True, related_name="drugs_for_disease")

    def _str_(self):
        return self.name

class Target(models.Model):
    TargetID = models.CharField(max_length=120)
    TargetName = models.CharField(max_length=120)
    Diseases = models.ManyToManyField(Disease, blank=True, related_name="targets_for_disease")
    Drugs = models.ManyToManyField(Drug, blank=True, related_name="targets_for_drug")

    def _str_(self):
        return self.name                
