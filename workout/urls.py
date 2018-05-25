
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('workout/', views.WorkoutView.as_view(), name='workout'),
    path('', views.HomeView.as_view(), name='home'),
    path('createworkout/', views.CreateWorkoutView.as_view(), name='createworkout'),
    path('workout/<int:pk>/', views.WorkoutDetailsView.as_view(), name='workoutdetails'),
]