from django.shortcuts import render
from django.views import generic

class RegisterView(generic.TemplateView):
	template_name = 'userprofile/register.html'

class LoginView(generic.TemplateView):
	template_name = 'userprofile/login.html'
# Create your views here.
