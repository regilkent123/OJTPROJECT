from rest_framework import serializers
from .models import Workout, WorkoutVideo

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


class WorkoutVideoSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)

    class Meta:
        model = WorkoutVideo
        fields = '__all__'
    workout = serializers.CharField(required=False)
