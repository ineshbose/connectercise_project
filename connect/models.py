from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateOfBirth = models.DateField(null=True, blank=True)
    profilePhoto = models.ImageField(null=True, blank=True, upload_to='static')
    sex = models.CharField(null=True, choices=[('F','Female'),('M','Male')], max_length=1)
    sport_choices = [('HIKE', 'Hiking'),('FB','Football'),('BB','Basketball'),('CYC','CYCLING')]
    sport_preference = models.CharField(max_length=4, choices=sport_choices)

    def __str__(self):
        return self.user.username

class Rating(models.Model):
    ratingUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratingUser')
    ratedUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratedUser')
    like = models.BooleanField()

    class Meta:
        unique_together = ('ratingUser', 'ratedUser')
    
    def __str(self):
        return str(self.ratingUser) + ' rating ' + str(self.ratedUser) + ' rated ' + str(self.like)

class Match(models.Model):
    user1 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user2')

    class Meta:
        unique_together = ('user1', 'user2')
        unique_together = ('user2', 'user1')
    
    def __str__(self):
        return str(self.user1) + ' matched ' + str(self.user2)