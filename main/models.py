from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include
    #username = models.CharField(max_length=128, default='connectercise')
    #password = models.CharField(max_length=128, default='password')
    #website = models.URLField(blank=True)
    #email = models.CharField(max_length=128, blank=True)
    #sport = models.CharField(max_length=128)
    #location = models.CharField(max_length=128)
    #picture = models.ImageField(upload_to='profile_images', blank=True)
    #socialMedia = models.CharField(max_length=128)
    #requests = models.ManyToManyField(SportingRequest, blank=True)
    #matches = models.ForeignKey(User, blank=True, on_delete = models.DO_NOTHING, related_name="matches", default=None)

    def __str__(self):
        return self.user.username
        
class SportingRequest(models.Model):
    #time = models.DateTimeField(auto_now=True,blank=True) # Blank since it can be optional
    location = models.CharField(max_length=128)
    sessionID = models.CharField(max_length=16, primary_key=True)
    sport = models.CharField(max_length=128)
    duration = models.DurationField(blank=True, default=1) # Blank since it can be optional
    status = models.BooleanField(default=True) # To see if request has been completed. True = Request open, False = Request closed
    start_user = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name="start_user", default=None)
    involved_users = models.ForeignKey(UserProfile, blank=True, on_delete = models.DO_NOTHING, related_name="involved_users", default=None)
    def __str__(self):
        return self.sessionID