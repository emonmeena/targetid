# Generated by Django 4.1.7 on 2023-03-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugdiscovery', '0006_drug_clinicalstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='DrugSMIL',
            field=models.CharField(default='default_value', max_length=500),
        ),
    ]