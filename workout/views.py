from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import WorkoutForm

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
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs) :
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/workout/')
        return render(request, self.template_name, {'form': form})
# Create your views here.
