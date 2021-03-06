from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from registration.signals import user_registered
import uuid

# Sport Model that contains Requests; the names are supposed to be unique
class Sport(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='sports', default='sports/default.jpg')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sport, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# Requests that belong to Sports; they have a unique ID generated through 'uuid' that are also used as slugs
class SportRequest(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    request_id = models.CharField(max_length=128,primary_key=True)
    suggested_date = models.DateField(null=True, blank=True, help_text='MM/DD/YY (optional HH:MM)')
    location = models.CharField(max_length=512)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1024)
    completed = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='requests', blank=True)

    def save(self, *args, **kwargs):
        self.request_id = str(uuid.uuid4().int)
        self.slug = slugify(self.request_id)
        super(SportRequest, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# UserProfile Model that contains 'auth_user', a picture and slug for their URL
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', default='profile_images/default.jpg')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

# Comment Model
class Comment(models.Model):
    request = models.ForeignKey(SportRequest,on_delete=models.CASCADE,related_name='comments')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

# Used to create a UserProfile after creating 'auth_user'
def createUserProfile(sender, user, request, **kwargs):
    UserProfile.objects.get_or_create(user=user)

user_registered.connect(createUserProfile)