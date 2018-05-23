
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('afterlogin/', views.AfterLoginView.as_view(), name='afterlogin'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    ]