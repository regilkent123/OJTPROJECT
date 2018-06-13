from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from opentok import OpenTok, MediaModes, OutputModes
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
        context = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': self.session_id,
            'token': token,
        }
        return render(request, 'videostream/publisher.html', context)

class SubscribeVideoView(ForFitView):

    def get(self, request, *args, **kwargs):
        token = opentok.generate_token(self.session_id)
        context = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': self.session_id,
            'token': token,
        }
        return render(request, 'videostream/subscriber.html', context)

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'workout/home.html'
    redirect_field_name = ''
    form_class = UserProfileForm

    def get_context_data(self):
        context = super().get_context_data()
        context['current_profile'] = self.request.user.userprofile
        return context

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
        print("here")
        print("start", vars(archive))
        archives = Archive.objects.create(archive_id=archive.id)
        archive_id=archive.id 
        return JsonResponse({'archive_id':archive_id})


class endArchiveView(LoginRequiredMixin, View):
    def get(self , request , *args , **kwargs):
        print(self.request.GET.get("archive_id"))
        archive_id = self.request.GET.get("archive_id")
        archive=opentok.stop_archive(archive_id)
        print(archive_id,archive.json())
        return HttpResponse('Stop recording')

# class listArchive(ForFitView):
#     def get(self , request , *args , **kwargs):
#         archive_id= self.request.GET.get("archive_id")
#         archive_list = opentok.list_archive()
#         archive=archive_list.items[i]

#         for archive in iter(archive_list):
#             pass

#         total = archive_list.total



class deleteArchive(LoginRequiredMixin, View):
    def get(self , request , *args , **kwargs):
        print(self.request.GET.get("archive_id"))
        archive_id = self.request.GET.get("archive_id")
        opentok.delete_archive(archive_id)
        return HttpResponse('Deleted recording') 































# def videoTitle (request, title_id):
#         title = get_object_or_404(Archive, pk=title_id)
#         archiveTitle=request.POST[]
#         return render(request, 'videostream/viewArchive.html',{'title': title})


# class history(ForFitView):
#     def get(self, request, *args, **kwargs):
#         # page = int(request.GET.get('page', '1'))
#         # archive_id = self.request.GET.get("archive_id")
#         # for archive_id in (self.session_id):
#         #     print (archive_id)
#         # # offset = (page - 1) * 5

#         # # context = {
#         # archives = opentok.get_archives(offset= offset, count=5)
#         # show_previous = '/videostream/history?page=' + str(page - 1) if page > 1 else None
#         # show_next = '/videostream/history?page=' + str(page+1) if archives.count > (offset + 5) else None
#         # # }
#         # return JsonResponse({'self.session_id':self.session_id})
#         # return render('videostream/history.html', {'archives': archives})
#     # def get(self, request, *args, **kwargs):

#         archive_list = opentok.list_archive(self.session_id)
        # pass

    #     total = archive_list.total
    #     return HttpResponse(total)

# class download(ForFitView):
#     def get(self, request, *args, **kwargs):
#         archive_id = self.request.GET.get("archive_id")
