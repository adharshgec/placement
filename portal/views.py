from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from job.models import Job, AppliedJob
from result.models import Result
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def url_redirect(request):
    return HttpResponseRedirect("/login")

def student_profile_view(request):    
    return render(request, 'student/profile.html')

def student_result_view(request):
    results = Result.objects.all()
    return render(request, 'student/result.html', {'results': results})

def student_job_view(request):
    applied_jobs = AppliedJob.objects.all()
    jobs = Job.objects.all()
    return render(request, 'student/job.html', {'jobs': jobs, 'applied_jobs': applied_jobs})

def student_applied_jobs(request):
    applied_jobs = AppliedJob.objects.all()
    jobs = Job.objects.all()
    return render(request, 'student/applied_jobs.html', {'jobs': jobs, 'applied_jobs': applied_jobs})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.rollno = form.cleaned_data.get('rollno')           
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('student-profile')
    else:
        form = SignUpForm()
    return render(request, 'student/signup.html', {'form': form})
