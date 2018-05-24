from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)
    workout_type = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = '__all__'

    workout_type = serializers.CharField(source = 'get_workout_type_display')