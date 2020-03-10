from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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
    title = models.CharField(max_length=128, unique=True)
    #url = models.URLField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1024, default='Enter description')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SportRequest, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username