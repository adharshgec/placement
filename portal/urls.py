from django.conf.urls import include, url
from portal.views import StudentProfileView, student_profile_view

urlpatterns = [
    url(r'^profile/$', student_profile_view, name='student-profile'),     
]
