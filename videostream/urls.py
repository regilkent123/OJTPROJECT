
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
	path('publish/', views.PublishVideoView.as_view(), name='publish'),
	path('subscribe/', views.SubscribeVideoView.as_view(), name='subscribe'),
    # path('startArchive/', views.startArchive, name='startArchive'),
    # path('endArchive/', views.endArchive, name='endArchive'),
    path('startArchive/', views.startArchiveView.as_view(), name='archive'),
    path('endArchive/', views.endArchiveView.as_view(), name='archive'),

]