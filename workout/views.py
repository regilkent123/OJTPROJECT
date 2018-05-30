from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import WorkoutForm
from workout.models import Workout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.forms import UserProfileForm

class WorkoutView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/workout.html'
    login_url = '/login/'
    redirect_field_name = ''

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/home.html'
    initial = {'key': 'value'}
    login_url = '/login/'
    redirect_field_name = ''
    form_class = UserProfileForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})

class CreateWorkoutView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/createworkout.html'
    initial = {'key': 'value'}
    form_class = WorkoutForm
    login_url = '/login/'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs) :
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/workout/')
        return render(request, self.template_name, {'form': form})

class WorkoutDetailsView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/workout_details.html'
    login_url = '/login/'
    redirect_field_name = ''
    pattern_name = 'workoutdetails'

    def get(self, request, *args, **kwargs):
        work = Workout.objects.get(pk=kwargs['pk'])
        return render(request, self.template_name,{'workout':work})

