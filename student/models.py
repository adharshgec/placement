from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    M = 'Male'
    F = 'Female'
    GENDER = {
        (M, 'Male'),
        (F, 'Female'),
    }        
    rollno = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=50)
    batch = models.CharField(max_length=4)
    gender = models.CharField(max_length=6, choices=GENDER, default=M)
    current_CGPA = models.DecimalField( max_digits=4, decimal_places=2)
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __unicode__(self):
        return unicode(self.rollno)
