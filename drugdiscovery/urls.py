from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('get_all_disease/<disease_name>', views.get_all_disease, name='get all disease'),
    path('get_all_drugs/<drug_name>', views.get_all_drugs, name='get all drugs'),
    path('create/', views.create_database, name='create database'),
    path('push_smil/', views.push_smil, name='push SMIL'),
    path('get_all_smil/<disease_name>', views.get_all_smil, name='get all SMIL structures'),
    # path('post_people/', views.post_people, name='post a new member'),
    # path('get_bloodtest_data/', views.get_bloodtest_data, name='get blood test data'),
    # path('get_xray_data/', views.get_xray_data, name='get xray'),
    # path('get_account_data/', views.get_account_data, name='get accounts'),
    # path('post_xray_data/', views.post_xray_data, name='post xray'),
    # path('post_bloodtest_data/', views.post_bloodtest_data, name='post bloodtest'),
    # path('post_account_data/', views.post_account_data, name='post account'),
]
