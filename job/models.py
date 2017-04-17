from django.db import models
from portal.models import Profile

class Job(models.Model):
    company_id = models.IntegerField(unique=True)
    company = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    minimum_cgpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.company_id) 

class AppliedJob(models.Model):
    student_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    student_applied_job = models.ForeignKey(Job, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.student_rollno)
