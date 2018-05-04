
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('afterlogin/', views.AfterLoginView.as_view(), name='afterlogin'),
    path('invalidlogin/', views.InvalidLoginView.as_view(), name='invalidlogin'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register')

]