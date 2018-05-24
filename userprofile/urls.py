

from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('afterlogin/', views.AfterLoginView.as_view(), name='afterlogin'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
<<<<<<< HEAD
    path('loggedin/', views.auth_login, name='loggedin'),
]
=======
    ]
>>>>>>> 10b635bbbb73c4f531a907defc1acfb798a7f203
