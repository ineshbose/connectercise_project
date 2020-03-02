from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    pageURL = models.CharField(max_length=128, unique=True)
    sport = models.CharField(max_length=128, unique=True)
    location = models.CharField(max_length=128, unique=True)
    socialMedia = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.username
        
class SportingRequest(models.Model):
    time = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=128, unique=True)
    sessionID = models.IntegerField(default=0)

    def __str__(self):
        return self.sessionID