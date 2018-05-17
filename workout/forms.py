from django import forms
from django.core.exceptions import ValidationError
from .models import Workout

class WorkoutForm(forms.ModelForm):
    
    class Meta:
        model = Workout
        fields = ['workout_name', 'workout_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


    def save(self):
        createworkout = Workout.objects.create(
        workout_name = self.cleaned_data.get('workout_name'),
        workout_type = self.cleaned_data.get('workout_type'),
        description = self.cleaned_data.get('description'),
        )
        return createworkout