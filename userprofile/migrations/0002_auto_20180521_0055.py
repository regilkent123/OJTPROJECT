# Generated by Django 2.0.4 on 2018-05-21 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usertype',
            field=models.IntegerField(choices=[(1, 'Trainee'), (2, 'Trainer')], default='Trainee', max_length=7),
        ),
    ]
