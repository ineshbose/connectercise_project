from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # The additional attributes we wish to include
    pageURL = models.URLField(blank=True)
    sport = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    socialMedia = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.user.username
        
class SportingRequest(models.Model):
    time = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=128)
    sessionID = models.CharField(max_length=16,primary_key=True)
    sport = models.CharField(max_length=128)

    def __str__(self):
        return self.sessionID