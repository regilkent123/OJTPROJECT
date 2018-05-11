from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

class RegisterView(generic.TemplateView):
    template_name = 'userprofile/register.html'
    form_class = RegisterForm
 

    def get(self, request, *args, **kwargs):

        return HttpResponseRedirect('/afterlogin/')


    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/afterlogin/')
        return render(request, self.template_name, {'form': form})

    # def registers(request):
    #     if request.method == 'POST':
    #         form = RegisterForm(request.POST)
    #
    #         if form.is_valid():
    #             form.save()
    #             username = form.cleaned_data.get('username')
    #             raw_password = form.cleaned_data.get('password')
    #             user = authenticate(username=username, password=raw_password)
    #             login(request, user)
    #             return HttpResponseRedirect('/afterlogin/')
    #
    #     else:
    #         form = RegisterForm()
    #     # only 79 char per line guys hahaha please don't go over 79 characters
    #     return render(request, '../templates/userprofile/register.html', {'form': form})






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
