# Generated by Django 2.0.4 on 2018-05-21 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20180521_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usertype',
            field=models.IntegerField(choices=[(1, 'Trainee'), (2, 'Trainer')], default=1),
        ),
    ]
