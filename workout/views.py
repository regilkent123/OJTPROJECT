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
from userprofile.serializers import UserProfileSerializer

class WorkoutView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/workout.html'
    redirect_field_name = ''

    def get_context_data(self):
        context = super().get_context_data()
        context['current_profile'] = self.request.user.userprofile
        return context

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/home.html'
    redirect_field_name = ''
    form_class = UserProfileForm

    def get_context_data(self):
        context = super().get_context_data()
        context['current_profile'] = self.request.user.userprofile
        return context
        

class CreateWorkoutView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/createworkout.html'
    initial = {'key': 'value'}
    form_class = WorkoutForm
    redirect_field_name = ''

class WorkoutDetailsView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/workout_details.html'
    redirect_field_name = ''
    pattern_name = 'workoutdetails'

    def get_context_data(self, pk):
        context = super().get_context_data()
        context['workout_id'] = pk
        context['current_profile'] = self.request.user.userprofile
        return context
# Create your views here.