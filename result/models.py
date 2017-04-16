from django.db import models
from django.utils import timezone

class Result(models.Model):
    result_detail = models.CharField(max_length=50, default="Result Details...")
    published_date = models.DateField(null=True, blank=True, default="Enter Date...")
    resultfile = models.FileField(upload_to='results/%Y/%m/%d')
