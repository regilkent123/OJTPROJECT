from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import WorkoutForm
from django.views import View, generic
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from opentok import OpenTok, MediaModes, Roles, OutputModes, ArchiveModes
from .models import Session


api_key = "46117232"
api_secret = "06742bb12faa60106b61af9bcfe82ffc211ca161"

opentok = OpenTok(api_key, api_secret)

class ForFitView(View):

    def dispatch(self, *args, **kwargs):
        print ('hello from the other side')

        return super().dispatch(*args, **kwargs)

class PublishVideoView(ForFitView):


    def dispatch(self, *args, **kwargs):
        print ('hello from the side B')
       
        return super(PublishVideoView, self).dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        
        return render(request, 'videostream/publisher.html', {})


class SubscribeVideoView(ForFitView):
    pass


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
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            workoutName = form.cleaned_data['workout_name']
            return HttpResponseRedirect('/workout/')
        return render(request, self.template_name, {'form': form})
# Create your views here.
