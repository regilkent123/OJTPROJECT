from django import forms
from django.core.exceptions import ValidationError
from workout.models import Workout

class WorkoutForm(forms.ModelForm):
    
    class Meta:
        model = Workout
        fields = ['workout_name', 'workout_type', 'description', 'workout_photo']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 10, 'rows': 20}),
        }

    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.fields['workout_type'].empty_label =  None