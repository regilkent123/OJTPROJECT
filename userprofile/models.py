from django.db import models

class UserProfile(models.Model):
	utype = (
			('Trainee','Trainee'),
			('Trainer','Trainer'),
		)
	usertype = models.CharField(max_length=7, choices=utype, default='Trainee')
	username = models.CharField(max_length=20, primary_key=True, unique=True)
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	age = models.IntegerField()
	address = models.CharField(max_length=100)
	email_add = models.EmailField(max_length=50)
	sex = (
		('M','Male'),
		('F','Female'),
	)
	gender = models.CharField(max_length=1, choices=sex)
	height = models.IntegerField()
	weight = models.IntegerField()
# Create your models here.
