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
from rest_framework.renderers import TemplateHTMLRenderer

class WorkoutView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/workout.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile)
        return render(request, self.template_name, {'serializer': serializer})

    def post(self, request, *args, **kwargs):
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile, request.POST)
        print (serializer.is_valid(), serializer.errors)
        if serializer.is_valid():
            serializer.save()
        return render(request, self.template_name, {'serializer': serializer})

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/home.html'
    redirect_field_name = ''
    form_class = UserProfileForm

    def get(self, request, *args, **kwargs):
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile)
        return render(request, self.template_name, {'serializer': serializer})

    def post(self, request, *args, **kwargs):
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile, request.POST)
        if serializer.is_valid():
            serializer.save()
        return render(request, self.template_name, {'serializer': serializer})
        

class CreateWorkoutView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/createworkout.html'
    initial = {'key': 'value'}
    form_class = WorkoutForm
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile)
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form,'serializer': serializer})

    def post(self, request, *args, **kwargs) :
        form = self.form_class(request.POST, request.FILES)
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile, request.POST)
        if serializer.is_valid():
            serializer.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/workout/')
        return render(request, self.template_name, {'form': form,'serializer': serializer})

class WorkoutDetailsView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/workout_details.html'
    redirect_field_name = ''
    pattern_name = 'workoutdetails'

    def get(self, request, *args, **kwargs):
        work = Workout.objects.get(pk=kwargs['pk'])
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile)
        return render(request, self.template_name,{'workout':work,'serializer': serializer})

    def post(self, request, *args, **kwargs):
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile, request.POST)
        if serializer.is_valid():
            serializer.save()
        return render(request, self.template_name, {'serializer': serializer})

# Create your views here.
