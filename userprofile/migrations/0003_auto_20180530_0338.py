# Generated by Django 2.0.4 on 2018-05-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20180524_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usertype',
            field=models.PositiveIntegerField(choices=[(1, 'Trainee'), (2, 'Trainer')], default=1),
        ),
    ]