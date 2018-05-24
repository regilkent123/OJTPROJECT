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

# usually ang name sa mga ingon ani nga view kay `Mixins`
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
    # def get(request):

    #     token= session.generate_token()
    #     content = {
    #         'api_key': api_key,
    #         'session_id': session_id,
    #         'token': token,
    #     }
    #     return render(request, 'videostream/subscriber.html', content)

class HomeView(TemplateView):
    template_name = 'videostream/lvs.html'