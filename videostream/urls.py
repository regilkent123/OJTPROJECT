
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
	path('publish/', views.PublishVideoView.as_view(), name='publish'),
	path('subscribe/', views.SubscribeVideoView.as_view(), name='subscribe'),
    # path('startArchive/', views.startArchive, name='startArchive'),
    # path('endArchive/', views.endArchive, name='endArchive'),

    # path('workout/', views.WorkoutView.as_view(), name='workout'),
    # path('home/', views.HomeView.as_view(), name='home'),
    # path('createworkout/', views.CreateWorkoutView.as_view(), name='createworkout'),


]