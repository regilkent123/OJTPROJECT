from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

class WorkoutView(generic.TemplateView):
	template_name = 'workout/workout.html'
# Create your views here.
