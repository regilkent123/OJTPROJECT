from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from opentok import OpenTok, MediaModes, Roles, OutputModes, ArchiveModes
from .models import Session, Archive
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.forms import UserProfileForm
from django.views import generic
from django.conf import settings

opentok = OpenTok(settings.OPENTOK_API_KEY, settings.OPENTOK_SECRET_KEY)


class ForFitView(LoginRequiredMixin, View):
    def dispatch(self, *args, **kwargs):
        session = Session.objects.filter(user=self.request.user.userprofile).first()

        if session:
            self.session_id = session.session_id
        else:

            session = opentok.create_session(media_mode=MediaModes.routed)
            sessions = Session.objects.create(session_id=session.session_id, 
                user=self.request.user.userprofile)
            self.session_id = sessions.session_id
        return super().dispatch(*args, **kwargs)


class PublishVideoView(ForFitView):

    def get(self, request, *args, **kwargs):
        token = opentok.generate_token(self.session_id)
        content = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': self.session_id,
            'token': token,
        }
        return render(request, 'videostream/publisher.html', content)


class SubscribeVideoView(ForFitView):

    def get(self, request, *args, **kwargs):
        token = opentok.generate_token(self.session_id)
        content = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': self.session_id,
            'token': token,
        }
        return render(request, 'videostream/subscriber.html', content)


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

class startArchiveView(ForFitView):
    def get(self, request, *args, **kwargs):
        print("Start archive")
        archive = opentok.start_archive(
            self.session_id,
            has_video=True,
            has_audio=True,
            name='Videos',
            output_mode=OutputModes.individual,
        )
        print("start", vars(archive))
        archives = Archive.objects.create(archive_id=archive.id)
        archive_id=archive.id 

        
        print("archive_id" , archive_id)
        return JsonResponse({'archive_id':archive_id})
  

class endArchiveView(LoginRequiredMixin, View):
    def get(self , request , *args , **kwargs):
        print(self.request.GET.get("archive_id"))
        archive_id = self.request.GET.get("archive_id")
        opentok.stop_archive(archive_id)
        return HttpResponse('Stop recording')


class deleteArchive(ForFitView):
    def get(self , request , *args , **kwargs):
        print(self.request.GET.get("archive_id"))
        archive_id = self.request.GET.get("archive_id")
        opentok.delete_archive(archive_id)
        return HttpResponse('Deleted recording')    

class listArchive(ForFitView):
    def get(self, request, *args, **kwargs):
        archive_list = opentok.list_archive()
        pass
        total = archive_list.total

