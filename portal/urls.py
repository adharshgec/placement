from django.conf.urls import include, url
from portal.views import student_profile_view, student_job_view, student_result_view
from job.views import student_job_apply

urlpatterns = [
    url(r'^profile/$', student_profile_view, name='student-profile'),   
    url(r'^result/$', student_result_view, name='student-result'),   
    url(r'^job/$', student_job_view, name='student-job'),
    url(r'^job_applied/$', student_job_apply, name='student-job-apply'),     
]
