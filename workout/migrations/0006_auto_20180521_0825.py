# Generated by Django 2.0.4 on 2018-05-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0005_auto_20180521_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_type',
            field=models.IntegerField(choices=[(1, 'Aerobic exercise'), (2, 'Strength exercise'), (3, 'Balance exercise'), (4, 'Flexibility exercise')], default=None),
        ),
    ]
