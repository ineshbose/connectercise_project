from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=128, primary_key=True)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64,unique=True)
    pageURL = models.CharField(max_length=128)
    sport = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    socialMedia = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.username
        
class SportingRequest(models.Model):
    time = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=128)
    sessionID = models.CharField(max_length=16,primary_key=True)
    sport = models.CharField(max_length=128)

    def __str__(self):
        return self.sessionID