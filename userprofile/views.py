from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# unsay error? wait gi close lagi nimo ang forms
#wala man kuya, naa ra gehapon
#AttributeError: 'str' object has no attribute 'get'
#unya ge highlight ang if form.is_valid()

class RegisterView(generic.TemplateView):
    template_name = 'userprofile/register.html'
    initial = {'key': 'value'}
    form_class = RegisterForm


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        print (form.is_valid(), form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password']
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/afterlogin/')
        return render(request, self.template_name, {'form': form})



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
