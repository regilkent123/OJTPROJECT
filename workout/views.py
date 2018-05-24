from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import WorkoutForm
from workout.models import Workout

class WorkoutView(generic.TemplateView):
    template_name = 'workout/workout.html'

class HomeView(generic.TemplateView):
    template_name = 'workout/home.html'

class CreateWorkoutView(generic.TemplateView):
    template_name = 'workout/createworkout.html'
    initial = {'key': 'value'}
    form_class = WorkoutForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        print(form.fields['workout_type'].choices)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs) :
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/workout/')
        return render(request, self.template_name, {'form': form})



def getwork(request,pk):
    template_name = 'workout/workout_details.html'
    work = Workout.objects.get(pk=pk)

    return render(request,template_name,{'workout':work})
# Create your views here.
