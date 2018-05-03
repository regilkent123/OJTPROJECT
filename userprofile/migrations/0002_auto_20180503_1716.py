# Generated by Django 2.0.4 on 2018-05-03 09:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
