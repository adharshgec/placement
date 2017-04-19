from django.shortcuts import render
from .models import AppliedJob

def student_job_apply(request):    
    student_job_object = AppliedJob(student_id=request.POST.get('id'), 
        student_applied_job=request.POST.get('applied-job'))
    student_job_object.save()    
    return render(request, 'student/job_applied.html')
