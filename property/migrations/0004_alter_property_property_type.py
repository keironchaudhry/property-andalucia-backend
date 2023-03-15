# Generated by Django 3.2.16 on 2023-03-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_property_post_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('apartment', 'Apartment'), ('flat', 'Flat'), ('townhouse', 'Townhouse'), ('villa', 'Villa'), ('residential housing estate', 'Residential Housing Estate'), ('country property', 'Country Property'), ('bungalow', 'Bungalow')], max_length=30),
        ),
    ]