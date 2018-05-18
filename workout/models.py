from django.db import models

class Workout(models.Model):
	workout_name = models.CharField(max_length = 200)
	workoutType = (
		('Aerobic exercise', 'Aerobic exercise'),
		('Strength exercise', 'Strength exercise'),
		('Balance exercise', 'Balance exercise'),
		('Flexibility exercise', 'Flexibility exercise'),
		)
	workout_type = models.CharField(max_length = 20, choices = workoutType)
	description = models.CharField(max_length = 150, blank = True, null = True)
	workout_photo = models.ImageField(upload_to = 'images/', null = True)
	def __str__(self):
		return workout_name
# Create your models here.
