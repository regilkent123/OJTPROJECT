from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path('workout/', views.WorkoutView.as_view(), name='workout'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('createworkout/', views.CreateWorkoutView.as_view(), name='createworkout'),
    path('coachpublish/', views.PublishVideoView.as_view(), name='coachpublish'),
    path('traineesubscribe/', views.SubscribeVideoView.as_view(), name='traineesubscribe'),

]