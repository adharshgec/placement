from django.db import models

class Result(models.Model):
    resultfile = models.FileField(upload_to='results/%Y/%m/%d')
