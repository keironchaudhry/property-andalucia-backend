# Generated by Django 3.2.16 on 2023-02-07 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20230201_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='post_code',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^\\d+$')]),
        ),
    ]
