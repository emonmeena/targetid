from django.contrib import admin
from .models import *

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'DiseaseID', 'DiseaseName')

class DrugAdmin(admin.ModelAdmin):
    list_display = ('id', 'DrugID', 'DrugName')

class TargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'TargetID', 'TargetName')            


admin.site.register(Disease)
admin.site.register(Drug)
admin.site.register(Target)


