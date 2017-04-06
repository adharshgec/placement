from django.conf.urls import include, url
from portal.views import StudentProfileView

urlpatterns = [
    url(r'^profile/$', StudentProfileView.as_view(), name='student-profile'),    
]
