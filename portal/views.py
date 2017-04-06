from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .models import Profile

class StudentProfileView(LoginRequiredMixin, ListView):
    """
    Student Profile for each student based on Login.
    """
    model = Profile
    # slug_field = 'rollno'
    template_name = 'student/profile.html'

def url_redirect(request):
    return HttpResponseRedirect("/login")

# def user_login(request):
#     context = RequestContext(request)
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user:               
#             login(request, user)             
#             return HttpResponseRedirect('student/profile.html')             
#         else:
#             print("Invalid login details: {0}, {1}".format(username, password))
#             return HttpResponse("Invalid login details: {0}, {1}".format(username, password))
#     else:
#         return render(request, 'registraion/login.html')

# def logout_view(request):
#     logout(request)
#     template = loader.get_template('registration/logged_out.html')
#     context = RequestContext(request)
#     return HttpResponse(template.render(context))
