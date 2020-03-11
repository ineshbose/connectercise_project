from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # The additional attributes we wish to include
    username = models.CharField(max_length=128, default='connectercise')
    password = models.CharField(max_length=128, default='password')
    pageURL = models.URLField(blank=True)
    email = models.CharField(max_length=128, blank=True)
    sport = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    socialMedia = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username

    
    class Meta:
        verbose_name_plural = 'users'  

    
class SportingRequest(models.Model):
    time = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=128)
    sessionID = models.CharField(max_length=16)
    sport = models.CharField(max_length=128)
    connected = models.BooleanField(default = False)

    def __str__(self):
        return self.sessionID

    class Meta:
        verbose_name_plural = 'requests'