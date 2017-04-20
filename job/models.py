from django.db import models
from portal.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Job(models.Model):
    company_id = models.IntegerField(unique=True)
    company = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    date_of_test = models.DateField(blank=True, null=True)
    minimum_cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    minimum_backlogs = models.IntegerField(default=1)

    def __str__(self):
        return str(self.company_id) 

class AppliedJob(models.Model):    
    student_id = models.CharField(max_length=30, blank=True)
    student_applied_job = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.student_applied_job)
