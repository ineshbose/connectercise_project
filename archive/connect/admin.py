from django.contrib import admin
from connect.models import UserProfile, Rating, Match

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Rating)
admin.site.register(Match)