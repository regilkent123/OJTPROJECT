
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('usertype', models.PositiveIntegerField(choices=[(1, 'Trainee'), (2, 'Trainer')], default=1)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('weight', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]