from django.shortcuts import render, redirect

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

class VideoStreamView(generic.TemplateView):
    template_name = 'videostreaming/vs.html'

# def login(request):
#     c= {}
#     c.update(csrf(request))
#     return render_to_request('login.html',c)
# def auth_view(request):
#     username=request.POST.get('username','')
#     password=request.POST.get('password','')
#     user=auth.authenticate(username=username, password=password)

#     if user is not None:
#         auth.login(request,user)
#         return HttpResponseRedirect('login/')
#     else :
#         return HttpResponseRedirect('invalidlogin/')

# def loggedin(request)
#     return render_to_response('loggedin.html',{'full_name' request.user.username})

# def invalid_login(request)
#     return to render_to_response('invalid_login.html')

# def logout(request)
#     auth.logout(request)
#     return to render_to_response('logout.html')
# # Create your views here.

