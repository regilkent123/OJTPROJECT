from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
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
        
        session = opentok.create_session(media_mode=MediaModes.routed,
            archive_mode=ArchiveModes.always)
    
    
        sessions = Session(session_id=session.session_id)
        sessions.save()
        session_id=session.session_id
        print ('session id:', session_id)
        # session_id = Session.objects.get(pk=1).session_id
        return super().dispatch(*args, **kwargs)

    # def dispatch(self, request, *args, **kwargs):
    #     # context = {}
    #     session = opentok.create_session(media_mode=MediaModes.routed,
    #         archive_mode=ArchiveModes.always)
    #
    #
    #     sessions = Session(session_id=session.session_id)
    #     sessions.save()
    #
    #     session_id = Session.objects.get(pk=1).session_id
    #     return (session_id)


class PublishVideoView(ForFitView):
        # and here we will override it again
    def dispatch(self, *args, **kwargs):
        print ('hello from the side B')
        # we call the original dispatch function here so it will act the same
        # as the regular View. same pud diri
        return super(PublishVideoView, self).dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        
    #     self. token = opentok.generate_token(sessions)
    #     content = {
    #         'api_key': api_key,
    #         'session_id': sessions,
    #         'token': token,
    #     }

        # return render(request, 'videostream/publisher.html', content)
        return render(request, 'videostream/publisher.html', {})


class SubscribeVideoView(ForFitView):

    def get(request):

        # token = opentok.generate_token(
        # session_id,
        # role=Roles.subscriber
        # )
        token= session.generate_token()
        content = {
            'api_key': api_key,
            'session_id': session_id,
            'token': token,
        }
        return render(request, 'videostream/subscriber.html', content)

class HomeView(TemplateView):
    template_name = 'videostream/lvs.html'
