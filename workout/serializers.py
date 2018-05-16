from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    detial_url = serializers.CharField(read_only=True)

    class Meta:
        model = Workout
        fields = '__all__'