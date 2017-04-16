from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollno = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    current_cgpa = models.DecimalField(max_digits=4, decimal_places=2, default=1.00)        

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
post_save.connect(create_or_update_user_profile, sender=User)