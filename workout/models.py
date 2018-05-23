from django.db import models

class Workout(models.Model):
    workout_name = models.CharField(max_length=200)
    AEROBIC = 1
    STRENGTH = 2
    BALANCE = 3
    FLEXIBILITY = 4
    workoutType = (
        (AEROBIC, 'Aerobic exercise'),
        (STRENGTH, 'Strength exercise'),
        (BALANCE, 'Balance exercise'),
        (FLEXIBILITY, 'Flexibility exercise'),
        )
    workout_type = models.PositiveIntegerField(choices=workoutType,blank=False,default=None)
    description = models.CharField(max_length=150,blank=True,null=True)
    workout_photo = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.workout_name

# Create your models here.
