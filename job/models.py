from django.db import models

class Job(models.Model):
    company_id = models.IntegerField(unique=True)
    company = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    minimum_cgpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __unicode__(self):
        return unicode(self.company_id) 

