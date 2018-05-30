from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import MinValueValidator
from datetime import date
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
            User, on_delete=models.CASCADE,
            primary_key=True,
        )

    TRAINEE = 1
    TRAINER = 2
    utype = (
            (TRAINEE,'Trainee'),
            (TRAINER,'Trainer'),
        )
    usertype = models.PositiveIntegerField(choices=utype,blank=False,default=TRAINEE)
    birthdate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    sex = (
        ('M','Male'),
        ('F','Female'),
    )
    gender = models.CharField(max_length=1, choices=sex, null=True, blank=True)
    height = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    weight = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    def __str__(self):
        return self.user.username

    def is_legal_age(self):
        now = date.today()
        age = now - self.birthdate
        return (age.days/365) >= 18

# Create your models here.
