from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

class RegisterView(generic.TemplateView):
    template_name = 'userprofile/register.html'

def register(request):
    usernames = request.POST['username']
    password = request.POST['password']
    firstname = request.POST['first_name']
    lastname = request.POST['last_name']
    email = request.POST['email']
    u=User(username=usernames, first_name=firstname, last_name=lastname, email=email)
    u.set_password(password)
    u.save()

    return HttpResponse('success')

class LoginView(generic.TemplateView):
    template_name = 'userprofile/login.html'


def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        auth_user = authenticate(username=username, password=password)

        if auth_user is not None:
            login(request, auth_user)
            return HttpResponseRedirect('/afterlogin/')
        else :
            return HttpResponse('error')
    return HttpResponse('not allowed') 

class AfterLoginView(generic.TemplateView):
    template_name = 'userprofile/loggedin.html'

class InvalidLoginView(generic.TemplateView):
    template_name = 'userprofile/invalid_login.html'

class LogOutView(generic.TemplateView):
    template_name = 'userprofile/logout.html'


# Create your views here.
