from django.db import models

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class SportRequest(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField() # Will be changed
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title