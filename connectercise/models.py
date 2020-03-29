from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from registration.signals import *
import uuid

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sport, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class SportRequest(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    request_id = models.CharField(max_length=128,primary_key=True)
    suggested_date = models.DateTimeField(null=True, blank=True, help_text='MM/DD/YY (optional HH:MM)')
    location_choices = [('England', 'England'),('Scotland', 'Scotland'),('Wales', 'Wales'),('Northern Ireland','Northern Ireland'),]
    location = models.CharField(max_length=128, choices=location_choices)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1024)
    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.request_id = str(uuid.uuid4().int)
        self.slug = slugify(self.request_id)
        super(SportRequest, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', default='profile_images/default.jpg')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    request = models.ForeignKey(SportRequest,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

def createUserProfile(sender, user, request, **kwargs):
    UserProfile.objects.get_or_create(user=user)

user_registered.connect(createUserProfile)