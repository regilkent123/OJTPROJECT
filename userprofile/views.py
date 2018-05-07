from django.shortcuts import render
from django.views import generic

class RegisterView(generic.TemplateView):
    template_name = 'userprofile/register.html'

class LoginView(generic.TemplateView):
    template_name = 'userprofile/login.html'


class AfterLoginView(generic.TemplateView):
    template_name = 'userprofile/loggedin.html'

class InvalidLoginView(generic.TemplateView):
    template_name = 'userprofile/invalid_login.html'

class LogOutView(generic.TemplateView):
    template_name = 'userprofile/logout.html'


# Create your views here.
