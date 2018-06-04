from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)

    class Meta:
        model = Workout
        fields = '__all__'
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

    workout_type = serializers.ChoiceField(choices=Workout.workoutType)
    workouttype = serializers.CharField(source='get_workout_type_display', required=False)