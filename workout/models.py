from django.db import models

class Workout(models.Model):
	workout_name = models.CharField(max_length = 200)
	aerobic = 1
	strength = 2
	balance = 3
	flexibility = 4
	workoutType = (
		(aerobic, 'Aerobic exercise'),
		(strength, 'Strength exercise'),
		(balance, 'Balance exercise'),
		(flexibility, 'Flexibility exercise'),
		)
	workout_type = models.IntegerField(choices = workoutType)
	description = models.CharField(max_length = 150, blank = True, null = True)
	workout_photo = models.ImageField(upload_to = 'images/', null = True)
	def __str__(self):
		return self.workout_name
# Create your models here.
