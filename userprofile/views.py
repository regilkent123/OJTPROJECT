from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

class RegisterView(TemplateView):
    template_name = 'userprofile/register.html'
    initial = {'key': 'value'}
    form_class = RegisterForm


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password']
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/afterlogin/')
            else:
                form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

class LoginView(TemplateView):
    template_name = 'userprofile/login.html'

    def post(self,request, *args, **kwargs):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            auth_user = authenticate(username=username, password=password)

        if auth_user is not None:
            login(request, auth_user)
            return HttpResponseRedirect('afterlogin')
        else :
            return HttpResponse('error')
        return HttpResponse('not allowed')

class AfterLoginView(TemplateView):
    template_name = 'userprofile/loggedin.html'

class LogOutView(TemplateView):
    def get(self,request):
        logout(request)
        return HttpResponse('LOGGED OUT!')


# Create your views here.
