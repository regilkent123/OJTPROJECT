# Generated by Django 2.0.4 on 2018-05-31 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videostream', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive_id', models.CharField(max_length=1000)),
            ],
        ),
    ]
