from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from job.models import Job
from result.models import Result


def url_redirect(request):
    return HttpResponseRedirect("/login")

def student_profile_view(request):    
    return render(request, 'student/profile.html')

def student_result_view(request):
    results = Result.objects.all()
    return render(request, 'student/result.html', {'results': results})

def student_job_view(request):
    jobs = Job.objects.all()
    return render(request, 'student/job.html', {'jobs': jobs})
