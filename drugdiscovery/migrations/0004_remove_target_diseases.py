# Generated by Django 4.1.7 on 2023-02-21 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drugdiscovery', '0003_target_diseases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target',
            name='Diseases',
        ),
    ]
