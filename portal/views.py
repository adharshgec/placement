from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from job.models import Job, AppliedJob
from result.models import Result


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
